# GraduateProject
마스크 인식 시스템 서버(Django) 

올해의 가장 큰 이슈라고 하면 코로나바이러스입니다. 코로나는 올 한 해 동안 우리 사회에 지대한 영향을 미쳤으며, 그로 인해 우리 사회에는 많은 변화가 생기게 되었습니다. 
그중 가장 눈에 띄는 변화라면 외출을 할 때면 항상 마스크를 착용한다는 점입니다. 이제 마스크 착용은 이제는 선택이 아닌 의무이며 많은 인원이 모이는 대중교통 등에는 마스크를 착용하지 않으면 입장조차 불가능합니다. 저희 팀은 이러한 상황에 맞추어 마스크 착용 여부를 인식하고 더 나아가 해당 데이터를 서버에 전송해 통계자료를 확보할 수 있는 시스템을 구현하고자 하였습니다. 

이를 통해 사람이 직접 상주하지 않아도 마스크 미 착용자의 입장을 통제할 수 있고 마스크 착용 비율을 수치화하여 통계화된 데이터를 코로나에 관련된 여러 기획에 참고가 될 수 있는 효과를 기대하였습니다.
해당 시스템은 전형적인 Server-Client구조를 가지며 아래는 대략적인 구성도입니다.
![마스크 클라이언트](https://user-images.githubusercontent.com/43844233/97338212-98bb4b00-18c4-11eb-8246-67288a9983eb.JPG)
해당 시스템의 클라이언트(각 역에 배치)는 그 자리에서 승객의 마스크를 카메라를 통해 인식하며 인식된 결과를 서버로 보내게 됩니다.  

![마스크 서버](https://user-images.githubusercontent.com/43844233/97338194-9527c400-18c4-11eb-90d4-0a25c995983a.JPG)
서버는 클라이언트에서 보내온 결과를 통해 총 인식인원과 마스크 착용인원의 수와 그것에 대한 비율을 집계하여 실시간 기록합니다.  

우선 웹캠을 통해 찍은 영상을 딥러닝 처리를 통해 마스크 유무를 확인 후 결과를 서버에 송신합니다. 
![aaa](https://github.com/user-attachments/assets/cd00b0c5-3606-46e9-87d9-82c962385e24)

딥러닝 작업은 실시간 객체 인식 프레임워크로 유명한 YOLO-Darknet를 통해 수행하였습니다.

같은 인물이 계속 영상 화면에 노출된다면 지속하여 서버에 결과값이 갱신되는 문제를 방지하기 위하여 인식 전후에 알람을 통해 처리가 완료된 인원은 화면 밖으로 이동할 수 있게 안내하였습니다.
처음 인식될때 인식중이라는 음성이 나오며 일정 시간 내내 마스크를 낀채로 인식이 유지되면 인식이 끝났고 지나가도 좋다는 음성이 나오고 서버로 정보가 집계됩니다.
만약 마스크를 착용하지 않은 채로 인식이 유지되면 마스크를 착용하라는 경고음성과 함께 역시 서버로 집계됩니다.  

서버에서는 관리자 계정으로 로그인을 통해 지역별 마스크 착용 여부에 대한 통계를 확인할 수 있게 구현하였습니다. 서버는 Django로 만든 웹서버이며 처음에 관리자인증을 위해 로그인합니다.

![서버 로그인](https://user-images.githubusercontent.com/43844233/97338266-a244b300-18c4-11eb-9027-c3ba3c813642.JPG)

그러면 이렇게 각 지역별 집계를 확인할 수 있습니다.

![서버그래프](https://user-images.githubusercontent.com/43844233/97338247-9eb12c00-18c4-11eb-8b47-ca96e0f09b00.JPG)

현재 추가된 기타 기능으로 Setting창에서 로그아웃과 Description창에서 간단한 프로젝트 정보를 확인할 수 있습니다.
![서버Setting](https://user-images.githubusercontent.com/43844233/97338278-a375e000-18c4-11eb-9c25-a0c3c98c0813.JPG)
![서버Description](https://user-images.githubusercontent.com/43844233/97338284-a40e7680-18c4-11eb-8aaf-bc4d1b2f9f2d.JPG)
