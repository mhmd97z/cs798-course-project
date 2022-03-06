### Useful links
- https://www.techplayon.com/5g-nr-rrc-procedure-states/


### RRC 
How both parties of UE and BS in the communication reach agreement on a common configuration. To do this, we need a special control mechanism to exchange informations on those configurations between communicating parties. The resulting implementation of this control mechanism is called RRC (Radio Resource Control). 

Another central role of RRC within each communicating party (i.e, within UE and Network) is to work as a control center for all of the lower layers within each system. The collection of all the lower layers within UE or basestation is called 'Radio Resource' (i.e, resources required to make radio communication possible). The major role of RRC is to control(configure) all the Radio Resources (PHY, MAC, RLC, PDCP) to make it possible to communicate between UE and the base station (e.g, gNB, eNB, NB, BTS etc).

The major functions of the RRC protocol include:
  - connection establishment and release functions
    - Addition, modification, and release of carrier aggregation
    - Addition, modification, and release of Dual Connectivity in NR or between E-UTRA and NR.
  - broadcast of system information
  - radio bearer establishment
  - reconfiguration and release
  - RRC connection mobility procedures
    - Handover and context transfer
    - UE cell selection and reselection and control of cell selection and reselection
    - Inter-RAT mobility
  - paging notification and release and outer loop power control

The operation of the RRC is guided by a state machine which defines certain specific states that a UE may be present in. The different RRC states in this state machine have different amounts of radio resources associated with them and these are the resources that the UE may use when it is present in a given specific state. There are three main states that the connection can have: 
  - connected
  - inactive (added in NR)
  - idle
When UE is power up it is in Disconnected mode/Idle mode, It can move  RRC connected with initial attach or with connection establishment. If there is no activity from UE for a short time, It can suspend its session by moving to RRC Inactive and can resume its session moving to RRC connected mode.

RRC Idle Mode Operations:
- PLMN selection
- Broadcast of system information
- Cell re-selection mobility
- Paging for mobile terminated data is initiated by 5GC
- Paging for mobile terminated data area is managed by 5GC
- DRX for CN paging configured by NAS
RRC Inactive Mode Operation:
- Broadcast of system information
- Cell re-selection mobility
- Paging is initiated by NG-RAN (RAN paging)
- RAN-based notification area (RNA) is managed by NG- RAN
- DRX for RAN paging configured by NG-RAN
- 5GC – NG-RAN connection (both C/U-planes) is established for UE
- The UE AS context is stored in NG-RAN and the UE
- NG-RAN knows the RNA which the UE belongs to
RRC Connected Mode Operation:
- 5GC – NG-RAN connection (both C/U-planes) is established for UE
- The UE AS context is stored in NG-RAN and the UE
- NG-RAN knows the cell which the UE belongs to
- Transfer of unicast data to/from the UE
- Network controlled mobility including measurements



- RRC.Conn.{Avg & Max}
- RRC.ConnEstabAtt.Sum
- RRC.ConnEstabSucc.Sum
- RRC.ConnReEstabAtt.{HOFail & Other & Sum & reconfigFail}
- RrcState -> CONNECTED, IDLE


**RRC Reconfiguration** is the most important steps in establishing Radio Connection between UE and Network. Connection reconfiguration is triggered by LTE or NR, and then the ue will send a connection reconfiguration complete message in response. After which, there will be an established connection. Needless to say, there's some initial configuration in the beginning [RRC Setup], and then you reconfigure that!

- The major functionality of RRC Reconfiguration and their operations:
  - Radio Bearer 
    - Establish
    - Modify
    - Release
  - Measurement 
    - Setup
    - Modify
    - Release
  - Scells or Cell Group 
    - Add
    - Modify
    - Release


### Carrier Aggregation
- [this link](https://info-nrlte.com/tag/secondary-cell-group/) 
- It aggregates multiple component carriers (CC), which can be jointly used for transmission to/from a single device. It combines two or more carriers into one data channel to enhance the data capacity of a network. -> Up to 16 carriers (contiguous and non-contiguous) can be aggregated, resulting in overall transmission bandwidths of up to 6,400 MHz (16 x 400 MHz).
- The carriers do not have to be contiguous in the frequency domain but can be dispersed, both in the same frequency band as well as in different frequency bands, resulting in three difference scenarios:
  - Intraband aggregation with frequency-contiguous component carriers;
  - Intraband aggregation with non-contiguous component carriers;
  - Interband aggregation with non-contiguous component carriers.
- A carrier-aggregation-capable device can receive and transmit from/to multiple cells. One of these cells is referred to as the primary cell (PCell). This is the cell which the device initially finds and connects to, after which one or more secondary cells (SCells) can be configured, once the device is in connected mode. The secondary cells can be rapidly activated or deceived to meet the variations in the traffic pattern. Furthermore, the number of carriers (or cells) does not have to be the same in UL and DL. 
- Carrier aggregation uses L1/L2 control signaling for the same reason as when operating with a single carrier. 
- As baseline, all the feedback is transmitted on the primary cell. But there are other considerations: for many downlink component carriers, a single uplink carrier may carry a large number of acknowledgments. To avoid overloading a single carrier, it is possible to configure two PUCCH groups where feedback relating to the first group is transmitted in the uplink of the PCell and feedback relating to the other group of carriers is transmitted on the primary second cell (PSCell).


### PCI conflict
Each LTE cell has two identifiers, with different purposes – the Global Cell ID and the PCI. The Global Cell ID is used to identify the cell from an Operations, Administration and Management (OAM) perspective. The PCI has a value in the range of 0 to 503, and is used to scramble the data in order to allow mobile phones to separate information from different eNB. Since a LTE network may contain a much larger number of cells than the 504 available numbers of PCIs, the same PCI must be reused by different cells.

However, an UE, which is any device used directly by an end-user to communicate, cannot distinguish between two cells if both have the same PCI and frequency bands; this phenomenon is called a PCI conflict. PCI conflicts can be divided into two situations – PCI confusions and PCI collisions.

A PCI confusion occurs whenever a E-UTRAN cell has two different neighbor E-UTRAN cells with equal PCI and frequency.

A PCI collision happens whenever a E-UTRAN cell has a neighbor E-UTRAN cell with identical PCI and frequency.



### Cell
- **Cell Global ID (CGI)**: Cell Global Identity (CGI) is a globally unique identifier for a Base Transceiver Station in mobile phone networks. It consists of four parts: Mobile Country Code (MCC), Mobile Network Code (MNC), Location Area Code (LAC) and Cell Identification (CI).
- **PLMN**: A PLMN ID is an ID that globally identifies a mobile operator (e.g. combination of MCC (450) and MNC (05) for SK Telecom in Korea).
- **cell individual offset**: CIO is a offset value which is added with the neighbors measurement value for HO decision. It's value can be positive or negative. So putting negative value will make the measurment value of the neighbor more weaker so less possibility of HO with that neighbor, while setting positive value will make the neighbor measurment value stronger so high possibility for HO with that neighbor. In huawei system, neighbor cells's measurement (for intra and inter freq HO) are measured by the sum of CIO+CIOoffset+actual measurement quantity of the neighbor. So in huawei, there are 2 parameters, one is CIO (which is cell oriented individual offset, defined per cell), another is CIOoffset (defined per neighbor).
- sCell and nCell 
- TxDB 
- Azimuth 
- Arc: 
- A3Offset: realted to HO 
- TTT: realted to HO 
- A3Hyst: realted to HO 
- PCellOffset: 
- Neighbors(NCellOffset): 
- FreqOffset: 
- **PCI**: The physical cell ID (PCI) is used to indicate the physical layer identity of the cell. The PCI is used for cell identity during cell selection procedure. The purpose of PCI optimization is to ensure to a great extent that neighboring cells should have different primary sequences allocated. Cleaning the PCIs is probably the most effective steps to improve RF performance. Good PCI assignment reduces call drops by enabling UE to clearly distinguish one cell from another. The PCI planning proposal for a LTE network deployment includes each site shall have unique physical layer cell identity group, ranging from [0 to 167] and each sector within a site shall have unique physical layer sub-cell identity, ranging from [0 to 2]. Usually, the proposed PCI percentage planned for in-building is 30% and outdoor cells is 70% of all available PCI.
- Cell NCGIs 



- ncgi [NR Cell Global Identifier (NCGI) is used to identify NR cells globally and is constructed from the PLMN ID the cell belongs to and the NR Cell Identity (NCI) of the cell]
- sector [a geographic area defined by WSP(according to WSP’s own radio frequency coverage data), and consisting of a certain portion or all of the total coverage area of a Cell Site]

- measurementparams:
  - timetotrigger: 0
  - frequencyoffset: 0
  - pcellindividualoffset: 0
  - ncellindividualoffsets: {}
  - hysteresis: 0
  - eventa3params:
    - a3offset: 0
    - reportonleave: false
- pci: The physical cell ID (PCI) is used to indicate the physical layer identity of the cell
- earfcn: 47
- celltype: 0 [FEMTO,ENTERPRISE,OUTDOOR_SMALL,MACRO]



### UE
- Reference Signals Received Power (**RSRP**) and Reference Signal Received Quality (**RSRQ**) are key measures of signal level and quality for modern LTE networks. 
  - In cellular networks, when a mobile device moves from cell to cell and performs cell selection/reselection and handover, it has to measure the signal strength/quality of the neighbor cells. In the procedure of handover, the LTE specification provides the flexibility of using RSRP, RSRQ, or both.
- **5QI** (5G QoS Identifier) is a pointer to a set of QoS characteristics such as priority level, packet delay or packet error rate, etc.
  - https://www.techplayon.com/5g-nr-standardized-qos-identifier-5gqi-to-qos-characteristics-mapping/
- **IMSI**: IMSI is a unique ID that globally identifies a mobile subscriber
- **CRNTI**: Cell RNTI (C-RNTI) is a unique identification used for identifying RRC Connection and scheduling which is dedicated to a particular UE. The gNB assigns different C-RNTI values to different UEs. The gNB uses C-RNTI to allocate a UE with uplink grants, downlink assignments, etc. C-RNTI is used by gNB to differentiate uplink transmissions (e.g. PUSCH, PUCCH) of a UE from others.

### EARFCN
- EARFCN stands for E-UTRA Absolute Radio Frequency Channel Number.In LTE, the carrier frequency in the uplink and downlink is designated by EARFCN, which ranges between 0-65535.
- EARFCN uniquely identify the LTE band and carrier frequency.
- For example Band-1 and Band-4 can have same Rx frequency 2110-2170 MHz,  but their EARFCN are different.
- EARFCN is independent of channel bandwidth.
- To check EARFCN value on an Android phone, use the LTE Discovery app, tap SIGNALS, check EARFCN(band number), ‘DL Freq and UL Freq’.
 
- The relation between EARFCN and its uplink/downlink carrier frequency is given by the equation below
Fdownlink=FDLLow+0.1(NDL−NDLOffset)Fdownlink=FDLLow+0.1(NDL-NDLOffset)
Fuplink=FULLow+0.1(NUL−NULOffset)

where,

NDL = downlink EARFCN
NUL = uplink EARFCN
NDLoffset = offset used to calculate downlink EARFCN
NULoffset = offset used to calculate uplink EARFCN
- EARFCN of carrier frequency can be calculated with Eq-(1) or Eq-(2) using FDL_low, NOffs-DL, FUL_low and NOffs-UL given in the table here: https://www.cablefree.net/wirelesstechnology/4glte/lte-carrier-frequency-earfcn/#:~:text=EARFCN%20stands%20for%20E%2DUTRA,LTE%20band%20and%20carrier%20frequency.
