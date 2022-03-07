## LTE Scheduling
Scheduling is a process through which eNodeB decides which UEs should be given resources (RBs), how much resource (RBs) should be given to send or receive data .In LTE, scheduling is done at per subframe basis i.e. every 1 mili second. The entity which is govern this is know as scheduler.

A scheduler 
- takes input from OAM as system configuration e.g. which scheduling algorithm is to be enable (round robin, Max C/I, Proportional Fair, QoS aware etc), 
- consider QoS information (Which QCI, GBR/N-GBR etc.) 
- and channel quality information (CQI, Rank, SINR etc) to make the decisions.

A LTE scheduler performs following function for efficient scheduling:
- Link Adaptation: It selects the optimal combination of parameters such as modulation, channel Coding & transmit schemes i.e. Transmission Mode (TM1/TM2/TM3/TM4) as a function of the RF conditions.
- Rate Control: It is in charge of resource allocation among radio bearers of the same UE which are available at the eNB for DL and at the UE for UL.
- Packet Scheduler: It arbitrates access to air interface resources on 1ms-TTI basis amongst all active Users
- Resource Assignment: It allocates air interface resources to selected active users on per TTI basis.
- Power Control: Provides the desired SINR level for achieving the desired data rate, but also controls the interference to the neighbouring cells.
- HARQ (ARQ + FEC): It allows recovering from residual errors by link adaptation.

Different Types of Schedulers:
- Round Robin: The RR scheduler selects and schedules UEs in a round robin manner, thereby creating an equal resource share. The disadvantage of this approach is that UEs with sub-optimalCQIs may be allocated Physical Radio Resources (PRBs), thus reducing the overall cell throughput.
- Max CQI : The max-CQI scheduler selects the schedulable UEs based on the experienced CQI. The UEs with the highest CQI therefore become candidates for scheduling thereby increasing the overall cell throughput. The disadvantage of this approach is that UEs with lower CQI are denied scheduling instances, thus being starved for throughput and leading to degraded user experience.
- Proportional Fair: The PFS is expected to strike a balance between the traditional Round Robin (RR) scheduler and the max Throughput Scheduler (also known max-CQI (Channel Quality Indicator) scheduler). The PFS scheduler performs in such a manner that it considers resource fairness as well as maximizing cell throughput (in addition to other possible

## LTE Services and Scheduling Mechanism:
The Services/ Applications are broadly classified into two categories as Real time services and Non-Real time services. 

Real time services includes Conversational Voice, Video Phony [Conversational Video], MPEG Video [Non Conversational Video], Real-time gaming etc. 

Non-Real time services include Voice Messaging, Buffered Streaming, ftp, www, email, Interactive gaming etc.

The data transmission characteristics of these services are: Delay tolerance, Data Packet Size [Fixed or Variable], Periodic or Aperiodic data transmission, Packet error loss rate, etc.

Some or all of these characteristics determine what kind of Packet schedulers are required at the LTE MAC to adhere to the required QoS requirements of the relevant applications.

LTE MAC supports the following three types of Scheduling:
- Dynamic Scheduling: Every TTI, MAC checks for the UEs to be scheduled, the Data Availability for each UE to be scheduled and the feedback from the UE on the Channel conditions. Based on these data, it can schedule the resources for the UE through the PDCCH. If data is not available, UE will not get scheduled. All Services can be scheduled using Dynamic Scheduling, but at the expense of the Control signalling [PDCCH Usage – a scarce resource].
- Persistent Scheduling: In this case, Packets are scheduled on a fixed basis, similar to the Circuit Switched fashion. Here, it does not depend on the Channel Condition. The Resource allocation remains constant for the period of the call.
- Semi-Persistent Scheduling: It is a Hybrid way of scheduling, which tries to overcome the drawbacks of the Dynamic Scheduling and the Persistent Scheduling.


## 5G NR Grant Free Dynamic Scheduling – Transmission without Grant
5G networks are expected to support applications demanding ultra-reliable and low latency communication services (URLLC). To support these kind of applications 5G-NR introduced grant free uplink transmission feature a.k.a. Transmission without grant (TWG). i.e. data transmission without resource request. Transmission without grant can avoid the regular handshake delay e.g. sending the scheduling request and waiting for UL grant allocation. Another advantage is that it can relax the stringent reliability requirements on control channels.


## Useful Links
- https://www.techplayon.com/lte-enodeb-scheduler-and-different-scheduler-type/
- https://www.techplayon.com/5g-nr-grant-free-dynamic-scheduling-transmission-without-grant-twg/
- https://www.rcrwireless.com/20210326/test-and-measurement/scheduling-in-5g-dss-lte-maturity-matters-a-lot-says-srg
- https://5g.systemsapproach.org/primer.html#scheduler
