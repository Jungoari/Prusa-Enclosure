# Prusa MK3S DIY Enclosure (Klipper-based)

본 레포지토리는 Prusa MK3S 3D 프린터를 기반으로  
**Klipper 펌웨어 전환 및 커스텀 챔버(Enclosure) 제작**을 진행하는 프로젝트를 다룹니다.

현재는 챔버 제작을 위한 사전 단계로서  
**메인보드 교체, Klipper 환경 구성, 기본 동작 검증 및 캘리브레이션**까지 완료된 상태이며,  
외형 프레임 제작은 진행 중입니다.

본 프로젝트는 단계별로 진행되며, 멀티 컬러(MMU) 개조는 별도의 레포지토리에서 관리할 예정입니다.

---

## Project Status

- Done | Klipper 펌웨어 전환 완료
- Done | 메인보드 교체 완료 (Einsy Rambo → SKR Mini E3 V3.0)
- Done | 기본 동작 검증 및 주요 캘리브레이션 완료
- .... | 챔버 외형 프레임 제작 진행 중
- .... | 전기 배선 및 임베디드 보드 연동 예정
- .... | 챔버 적용 후 출력 테스트 예정

---

## Workflow

1. Prusa MK3S Klipper 펌웨어 전환 (완료)
2. 챔버 외형 프레임 주문 및 제작 (진행 중)
3. 전기 배선 작업 및 임베디드 보드 코딩 (예정)
4. 실제 출력 테스트 및 적용 (예정)

---

## System Overview

### Firmware & Software Stack

- Firmware: Klipper
- Host OS: Linux (Raspberry Pi)
- UI: Fluidd
- Installation Tool: KIAUH
- Slicer: Orca Slicer

Klipper는 Marlin 기반 펌웨어 대비  
가속도, 속도, 제어 파라미터 설정의 자유도가 높고  
웹 기반 UI를 통해 외부 디스플레이 및 챔버 연동에 용이하여 채택하였습니다.

---

## Hardware Configuration

### Mainboard Replacement

- 기존 Einsy Rambo 보드 제거
- BigTreeTech SKR Mini E3 V3.0 보드로 교체
- 모든 모터 및 센서 배선 JST 커넥터 기준으로 재작업
- 모터 및 센서별 라벨링 후 재배선

본 작업 과정에서 프린터를 완전 분해 및 재조립하였으며,  
이를 통해 Prusa MK3S 기구 구조 및 배선 구성 전반을 재정의하였습니다.

(사진 추가 예정)

---

### Motor & Endstop Configuration

- Prusa MK3S 센서리스 엔드스탑 방식 유지
- 스텝모터 배선 순서(1A–2A–1B–2B) 보드 기준 재정렬
- 센서리스 엔드스탑 점퍼 설정 및 Klipper 설정 반영

(사진 추가 예정)

---

### Fan & Power Configuration

- 기존 5V 팬 제거
- 노즐 팬 및 출력물 냉각 팬 모두 12V 팬으로 교체
- 전원은 PSU에서 SKR 보드로 직접 공급
- Raspberry Pi는 USB를 통해 SKR 보드와 연결

(사진 추가 예정)

---

## Sensor & Heater Verification

- 베드 서미스터 및 노즐 서미스터 정상 동작 확인
- 히터 카트리지 가열 테스트 완료
- 노즐 온도 45°C 이상 시 냉각 팬 자동 동작 설정

(사진 추가 예정)

---

## Calibration

### Completed

- PID Calibration
- Extruder Rotation Distance (E-step)
- Z-offset Calibration
- Bed Mesh Calibration
- Slicer 설정 수정 (Marlin → Klipper 기준)
- Flow Rate
- Pressure Advance
- Toolhead Alignment
- Origin (0,0) Offset Correction



캘리브레이션 과정은 단일 항목이 아닌  
기구적, 전기적, 소프트웨어 설정이 복합적으로 영향을 미치므로  
각 항목을 반복적으로 검증하며 진행 중입니다.

(사진 추가 예정)

---

## Known Issues & Mitigation

- 배선 오류가 소프트웨어 문제로 오인될 수 있음
- 캘리브레이션 항목 간 상호 의존성 존재
- 히터 및 노즐 체결 불량 시 누설 및 출력 품질 저하 발생 가능

해당 이슈들은 재조립 및 재설정을 통해 순차적으로 해결되었습니다.

---

## Enclosure (Chamber)

### Current Status

- 알루미늄 프로파일 기반 프레임 설계
- 챔버용 브라켓 모델링 및 출력
- 강화유리 및 포맥스 패널 치수 측정 및 구매
- 힌지 및 U형 가스켓 구매

(사진 추가 예정)

### Planned

- 챔버 내부 디스플레이 교체 (터치 지원)
- Fluidd UI 상시 표시
- 전면 개폐 구조 적용

---

## Future Work

- 챔버 안정화 이후 멀티 컬러(MMU) 개조 진행
  - 별도 레포지토리에서 관리
- 챔버 내부 환경 제어 기능 확장
- UI 커스터마이징

---

## Notes

본 문서는 프로젝트 진행 상황을 기술적으로 정리하기 위한 문서이며,  
완성 단계에 따라 지속적으로 업데이트됩니다.

---

# Q&A

- 질문 또는 기술적 문의는 아래 이메일로 연락 주세요.
- jw6258@sch.ac.kr

---