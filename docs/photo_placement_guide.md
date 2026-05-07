# Photo Placement Guide for `Prusa Enclosure V1.0`

이 문서는 `README.md`와 `docs/` 문서에 넣을 사진 파일의 위치, 목적, 촬영 가이드를 정리한 것입니다.

---

## Naming Rule

권장 파일명 규칙:

```text
docs/images/<number>_<short_description>.<jpg|png>
```

예시:

```text
docs/images/01_overall_enclosure.jpg
docs/images/04_skr_mini_e3_v3_wiring.jpg
docs/images/14_telegram_alert.jpg
docs/images/20_failure_probability_plot.png
```

사진은 가능하면 `jpg`, 그래프/스크린샷/회로도는 `png`를 권장합니다.

---

## README Photo Placement Table

| # | README Section | Image Path | Purpose | What to Show |
|---:|---|---|---|---|
| 01 | Title | `docs/images/01_overall_enclosure.jpg` | 프로젝트 대표 이미지 | 인클로저 전체 외관, Prusa MK3S가 내부에 보이도록 촬영 |
| 02 | Project Overview | `docs/images/02_system_overview.jpg` | 전체 시스템 이해 | 프린터, 인클로저, 센서, Raspberry Pi, 필터가 한 장면에 보이도록 구성 |
| 03 | System Architecture | `docs/images/03_wiring_data_flow.jpg` | 배선/데이터 흐름 | Raspberry Pi, Arduino, SKR 보드, 센서 연결 구조 |
| 04 | Hardware Configuration | `docs/images/04_skr_mini_e3_v3_wiring.jpg` | 보드 개조 증거 | SKR Mini E3 V3.0 장착, 케이블 라벨, 드라이버/커넥터 근접샷 |
| 05 | Hardware Configuration | `docs/images/05_sensor_hub_wiring.jpg` | 센서 허브 구성 | PMS7003, SGP30, DHT22, OLED/MAX7219 연결 상태 |
| 06 | Firmware & Control | `docs/images/06_klipper_moonraker_status.jpg` | Klipper 전환 확인 | Klipper/Moonraker 상태 화면, 터미널, Mainsail/Fluidd 화면 `((확인 필요))` |
| 07 | Enclosure Design | `docs/images/07_lower_printing_room.jpg` | 하단 Printing Room | 프린터가 놓인 하단 챔버, 팬/덕트/센서 위치 |
| 08 | Enclosure Design | `docs/images/08_upper_filament_room.jpg` | 상단 Filament Room | 필라멘트 보관부, 습도 관리 공간, 상하 분리 구조 |
| 09 | Air Filtration System | `docs/images/09_filter_module.jpg` | 필터 모듈 | HEPA + 활성탄 필터, 팬, 덕트, 리듀서 조립체 |
| 10 | Air Filtration System | `docs/images/10_pre_post_filter_sensors.jpg` | 필터 효율 분석 구조 | 필터 선단/후단 센서 모듈 위치 비교 |
| 11 | SimScale CFD Plan | `docs/images/11_simscale_airflow_model.png` | 유동 해석 계획 | 120 mm fan, 120→40 mm reducer, 40 mm pipe CAD/CFD 모델 |
| 12 | Sensor Monitoring System | `docs/images/12_sensor_logging_terminal.jpg` | 데이터 수집 증거 | UART JSON 로그, 1초 간격 기록, 센서 값 출력 터미널 |
| 13 | Nozzle Clogging Detection | `docs/images/13_nozzle_clogging_experiment.jpg` | 실험 장면 | 노즐 막힘 실험 중인 프린터, 출력물, 센서 위치 |
| 14 | Alert System | `docs/images/14_telegram_alert.jpg` | 경고 시스템 | Telegram Bot 알림 스크린샷, failure probability 포함 |
| 15 | Display / Dashboard UI | `docs/images/15_oled_project_title.jpg` | OLED 타이틀 | `Prusa Enclosure V1.0 / By Jeongwon Choi` 표시 화면 |
| 16 | Display / Dashboard UI | `docs/images/16_max7219_display.jpg` | 7-segment UI | DHT31 온도와 DHT33 습도 표시 장면 |
| 17 | Display / Dashboard UI | `docs/images/17_lcd_dashboard_printing.jpg` | 출력 중 대시보드 | SoC 온도, 스로틀링, CPU 부하, Moonraker 출력 상태 |
| 18 | Display / Dashboard UI | `docs/images/18_lcd_dashboard_idle.jpg` | 대기 화면 | 검정 배경, 주황색 `PRUSA Enclosure / by Jeongwon Choi` |
| 19 | Experimental Setup | `docs/images/19_normal_vs_clogging_print.jpg` | 정상/막힘 비교 | 정상 출력물과 막힘 출력물 비교 사진 |
| 20 | Results | `docs/images/20_failure_probability_plot.png` | 노즐 막힘 감지 결과 | 시간에 따른 failure probability, 실제 막힘 시점, 조기 경고 시점 |
| 21 | Results | `docs/images/21_filter_efficiency_plot.png` | 필터 성능 결과 | upstream/downstream PM 또는 TVOC 비교 그래프 |
| 22 | Photos / Build Log | `docs/images/22_build_process_collage.jpg` | 제작 과정 요약 | 프레임, 배선, 필터, 센서, UI를 모은 콜라주 |

---

## Recommended Extra Photos for `docs/build_log.md`

| Image Path | Use |
|---|---|
| `docs/images/build_01_original_prusa_mk3s.jpg` | 개조 전 Prusa MK3S 상태 |
| `docs/images/build_02_board_removed.jpg` | 기존 보드 제거 과정 |
| `docs/images/build_03_skr_mounting_bracket.jpg` | SKR Mini E3 V3.0 장착 브래킷 또는 고정 방식 |
| `docs/images/build_04_sensorless_homing_test.jpg` | X/Y 센서리스 홈 테스트 장면 |
| `docs/images/build_05_enclosure_frame.jpg` | 인클로저 프레임 조립 |
| `docs/images/build_06_panel_installation.jpg` | 패널/문/힌지 설치 |
| `docs/images/build_07_filter_cartridge.jpg` | HEPA + 활성탄 필터 카트리지 |
| `docs/images/build_08_duct_reducer_pipe.jpg` | 120 mm → 40 mm 리듀서와 40 mm 파이프 |
| `docs/images/build_09_sensor_module_inside.jpg` | 챔버 내부 센서 모듈 |
| `docs/images/build_10_sensor_module_filter_output.jpg` | 필터 후단 센서 모듈 |
| `docs/images/build_11_raspberry_pi_mount.jpg` | Raspberry Pi 장착 위치 |
| `docs/images/build_12_display_panel.jpg` | OLED / 7-segment / LCD 통합 패널 |
| `docs/images/build_13_cable_management.jpg` | 케이블 정리 및 라벨링 |
| `docs/images/build_14_first_power_on.jpg` | 최초 전원 인가 / 부팅 화면 |
| `docs/images/build_15_first_logged_print.jpg` | 첫 데이터 로깅 출력 |

---

## Photo Quality Checklist

- 전체샷은 프로젝트 구조가 한눈에 보이도록 넓게 촬영합니다.
- 보드/센서/배선 사진은 케이블 라벨이 읽힐 정도로 가깝게 촬영합니다.
- 디스플레이 사진은 화면 반사가 적은 각도에서 촬영합니다.
- Telegram, Klipper, 로그 화면은 개인정보와 토큰을 가린 뒤 업로드합니다.
- 실험 그래프는 축 이름, 단위, 범례, 실험 조건을 포함합니다.
- 불확실하거나 임시 배선인 사진에는 README 설명에서 `prototype`, `WIP`, `temporary wiring`이라고 표시합니다.

---

## Suggested Captions

아래 문구를 README 이미지 아래 캡션으로 사용할 수 있습니다.

```markdown
*Overall view of Prusa Enclosure V1.0 with the lower Printing Room and upper Filament Room.*
```

```markdown
*SKR Mini E3 V3.0 conversion for Klipper-based control of the Prusa MK3S platform.*
```

```markdown
*Upstream and downstream sensor modules for filter efficiency and breakthrough analysis.*
```

```markdown
*Real-time 1 Hz sensor and Moonraker metadata logging pipeline running on Raspberry Pi.*
```

```markdown
*Telegram Bot alert generated from the nozzle clogging failure probability threshold.*
```

---

## Minimum Photo Set for a Strong First GitHub Release

사진이 많지 않다면, 아래 8장만 먼저 넣어도 포트폴리오 완성도가 크게 올라갑니다.

1. `01_overall_enclosure.jpg`
2. `04_skr_mini_e3_v3_wiring.jpg`
3. `05_sensor_hub_wiring.jpg`
4. `09_filter_module.jpg`
5. `10_pre_post_filter_sensors.jpg`
6. `15_oled_project_title.jpg`
7. `17_lcd_dashboard_printing.jpg`
8. `20_failure_probability_plot.png`
