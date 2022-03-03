### RRC 
How both parties of UE and BS in the communication reach agreement on a common configuration. To do this, we need a special control mechanism to exchange informations on those configurations between communicating parties. The resulting implementation of this control mechanism is called RRC (Radio Resource Control). 

Another central role of RRC within each communicating party (i.e, within UE and Network) is to work as a control center for all of the lower layers within each system. The collection of all the lower layers within UE or basestation is called 'Radio Resource' (i.e, resources required to make radio communication possible). The major role of RRC is to control(configure) all the Radio Resources (PHY, MAC, RLC, PDCP) to make it possible to communicate between UE and the base station (e.g, gNB, eNB, NB, BTS etc).

There are three main states that the connection can have: 
  - connected
  - inactive (added in NR)
  - idle

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


## Carrier Aggregation
- [this link](https://info-nrlte.com/tag/secondary-cell-group/) 
- It aggregates multiple component carriers (CC), which can be jointly used for transmission to/from a single device. It combines two or more carriers into one data channel to enhance the data capacity of a network. -> Up to 16 carriers (contiguous and non-contiguous) can be aggregated, resulting in overall transmission bandwidths of up to 6,400 MHz (16 x 400 MHz).
- The carriers do not have to be contiguous in the frequency domain but can be dispersed, both in the same frequency band as well as in different frequency bands, resulting in three difference scenarios:
  - Intraband aggregation with frequency-contiguous component carriers;
  - Intraband aggregation with non-contiguous component carriers;
  - Interband aggregation with non-contiguous component carriers.
- A carrier-aggregation-capable device can receive and transmit from/to multiple cells. One of these cells is referred to as the primary cell (PCell). This is the cell which the device initially finds and connects to, after which one or more secondary cells (SCells) can be configured, once the device is in connected mode. The secondary cells can be rapidly activated or deceived to meet the variations in the traffic pattern. Furthermore, the number of carriers (or cells) does not have to be the same in UL and DL. 
- Carrier aggregation uses L1/L2 control signaling for the same reason as when operating with a single carrier. 
- As baseline, all the feedback is transmitted on the primary cell. But there are other considerations: for many downlink component carriers, a single uplink carrier may carry a large number of acknowledgments. To avoid overloading a single carrier, it is possible to configure two PUCCH groups where feedback relating to the first group is transmitted in the uplink of the PCell and feedback relating to the other group of carriers is transmitted on the primary second cell (PSCell).


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
