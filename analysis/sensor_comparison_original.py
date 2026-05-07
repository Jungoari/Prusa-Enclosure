import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 파일명
file1 = "sensor1.csv"
file2 = "sensor2.csv"

START_TIME = pd.Timestamp("2026-04-02 00:00:00")
PLOT_START_TIME = pd.Timestamp("2026-04-03 18:47:30")

def read_raw_time(path):
    df = pd.read_csv(
        path,
        usecols=['timestamp'],
        engine='python',
        on_bad_lines='skip'
    )
    time_col = df.columns[0]
    df[time_col] = pd.to_datetime(
        df[time_col],
        format="%Y-%m-%d %H:%M:%S",
        errors="coerce"
    )
    return df[[time_col]].dropna(), time_col

def load_csv(path):
    df = pd.read_csv(
        path,
        usecols=['timestamp', 'TVOC_ppb', 'eCO2_ppm'],
        engine='python',
        on_bad_lines='skip'
    )

    # 1열: 시간
    time_col = df.columns[0]
    df[time_col] = pd.to_datetime(
        df[time_col],
        format="%Y-%m-%d %H:%M:%S",
        errors="coerce"
    )

    # 5열, 6열
    col5 = 'TVOC_ppb'
    col6 = 'eCO2_ppm'

    df[col5] = pd.to_numeric(df[col5], errors='coerce')
    df[col6] = pd.to_numeric(df[col6], errors='coerce')

    # 10000 초과는 결측 처리
    df.loc[df[col5] > 10000, col5] = pd.NA
    df.loc[df[col6] > 10000, col6] = pd.NA

    # 4/2 이후만
    df = df[df[time_col] >= START_TIME]

    return df, time_col, col5, col6

# 플롯 데이터를 끝까지 0으로 확장
def extend_plot_df(df, time_col, value_col, end_time):
    df = df.sort_values(time_col)
    if df.empty:
        return pd.DataFrame({time_col: [START_TIME, end_time], value_col: [0.0, 0.0]})

    last_time = df[time_col].max()
    if last_time < end_time:
        fill = pd.DataFrame({
            time_col: [end_time],
            value_col: [0.0]
        })
        df = pd.concat([df, fill], ignore_index=True)
    return df

# 원본 시간 범위 계산용
raw1, raw_time1 = read_raw_time(file1)
raw2, raw_time2 = read_raw_time(file2)

raw1 = raw1[raw1[raw_time1] >= START_TIME]
raw2 = raw2[raw2[raw_time2] >= START_TIME]

GLOBAL_END_TIME = max(raw1[raw_time1].max(), raw2[raw_time2].max())

# 실제 plotting용 데이터
df1, time1, col5_1, col6_1 = load_csv(file1)
df2, time2, col5_2, col6_2 = load_csv(file2)

# 5열용 데이터
plot5_df1 = extend_plot_df(df1[[time1, col5_1]].dropna(), time1, col5_1, GLOBAL_END_TIME)
plot5_df2 = extend_plot_df(df2[[time2, col5_2]].dropna(), time2, col5_2, GLOBAL_END_TIME)

# 6열용 데이터
plot6_df1 = extend_plot_df(df1[[time1, col6_1]].dropna(), time1, col6_1, GLOBAL_END_TIME)
plot6_df2 = extend_plot_df(df2[[time2, col6_2]].dropna(), time2, col6_2, GLOBAL_END_TIME)

# 5번째 열 그래프
plt.figure(figsize=(12, 5))
plt.plot(plot5_df1[time1], plot5_df1[col5_1], label=f"{file1} - {col5_1}")
plt.plot(plot5_df2[time2], plot5_df2[col5_2], label=f"{file2} - {col5_2}")
plt.xlim(PLOT_START_TIME, GLOBAL_END_TIME)
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("5th Column vs Time")
plt.legend()
plt.grid(True)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m-%d %H:%M"))
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()

# 6번째 열 그래프
plt.figure(figsize=(12, 5))
plt.plot(plot6_df1[time1], plot6_df1[col6_1], label=f"{file1} - {col6_1}")
plt.plot(plot6_df2[time2], plot6_df2[col6_2], label=f"{file2} - {col6_2}")
plt.xlim(PLOT_START_TIME, GLOBAL_END_TIME)
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("6th Column vs Time")
plt.legend()
plt.grid(True)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m-%d %H:%M"))
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()