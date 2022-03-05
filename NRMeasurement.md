## Useful links
- https://www.techplayon.com/5g-nr-measurement-events/
- https://www.powerstream.com/watts-and-dbm-for-radio.htm
- https://www.techplayon.com/5g-nr-measurement-serving-cell-and-neighbor-cell/

## Basics
In any telecom technology (2G, 3G, 4G or 5G), mobility (handover) decision whether mobile device will be handover or not is taken by base station based on measurement reports from the mobile device. 

There are multiple measurement items (RSRP, RSRQ, SINR) and multiple ways (periodic, event triggered) to measure the signal quality of the serving cell and neighbor cells.

In Ideal case, a base station shall allow UE to report serving cell and neighbor cell signal quality and trigger the handover with single measurement, but in practice it can create overload conditions due to unnecessary ping pong handovers. As solution to avoid such situation, 3GPP specifications have proposed a set of predefined set of measurement report mechanism to be performed by UE. These predefined measurement report type is called “Event“. The type of “event” a UE have to report is specified by RRC signaling message sent by the base station.

3GPP specification 38.331 specified following events defined for 5G NR.
- Event A1 (Serving becomes better than threshold)
- Event A2 (Serving becomes worse than threshold)
- Event A3 (Neighbor becomes offset better than SpCell)
- Event A4 (Neighbor becomes better than threshold)
- Event A5 (SpCell becomes worse than threshold1 and neighbor becomes better than threshold2)
- Event A6 (Neighbour becomes offset better than SCell)
- Event B1 (Inter RAT neighbour becomes better than threshold)
- Event B2 (PCell becomes worse than threshold1 and inter RAT neighbor becomes better than threshold2)

If we closely  observed these event, we can categories them A1-A6 as Same RAT and B1-B2 as Inter RAT Events. UE keeps on measuring serving cell and neighbors report quantity and validate it with the threshold or offset defined in report configuration. The report quantity/the trigger for event can be RSRP, RSRQ or SINR.

## Measurment variables
- RSSI – Received Signal Strength Indicator
  - Measures the average total received power observed only in OFDM symbols containing reference symbols
- RSRP – Reference Signal Received Power
  - RSRP is a RSSI type of measurement
  - It is the power of the LTE Reference Signals spread over the full bandwidth and narrowband.
- RSRQ – Reference Signal Received Quality
  - Quality considering also RSSI and the number of used Resource Blocks (N) RSRQ = (N * RSRP) / RSSI measured over the same bandwidth. 
  - RSRQ is a C/I type of measurement and it indicates the quality of the received reference signal. 
  - The RSRQ measurement provides additional information when RSRP is not sufficient to make a reliable handover or cell reselection decision. 

In the procedure of handover, the LTE specification provides the flexibility of using RSRP, RSRQ, or both. 


## Event A1 (Serving becomes better than threshold)
Event A1 is triggered when the serving cell becomes better than a threshold. It is typically used to cancel an ongoing handover procedure. This may be required if a UE moves towards cell edge and triggers a mobility procedure, but then subsequently moves back into good coverage before the mobility procedure has completed.

```Ms – Hys >  Thresh           (Trigger Condition)
Ms + Hys <  Thresh           (Cancellation  Condition)
```
- **Ms** is the measurement result of the serving cell without taking any offsets into account. Ms can be expressed in dBm in case of RSRP, or in dB in case of RSRQ and RS-SINR
- **Hys** is the hysteresis parameter for A1 event expressed in dB. Hysteresis is signaled within reportConfigNR value between 0 and 30, Actual value in dB can be obtained by multiplying 0.5 with signal values e.g. signaled value is 5 then Hyst= 5 x 0.5 =2.5dB.
- **Thresh** is the threshold parameter for this event i.e. a1-Threshold as defined within reportConfigNR, Thresh is expressed in the same unit as Ms

## Event 2 (Serving becomes worse than threshold)
Event A2 is typically used to trigger a mobility procedure when a UE moves towards cell edge. Event A2 does not involve any neighbor cell measurements so it may be used to trigger a blind mobility procedure, or it may be used to triggers neighbor cell measurements which can then be used for a measurement based mobility procedure.

The detail is the same as A1! 

## Event A3 (Neighbor becomes offset better than SpCell)
Event A3 is triggered when a neighbor cell becomes better than a special cell (SpCell) by an offset. A special cell is the primary serving cell of either the Master Cell Group (MCG) or Secondary Cell Group (SCG)). The offset can be either positive or negative.

This event is typically used for intra-frequency or inter-frequency handover procedures. When Evenet A2 is triggered  the UE may be configured with measurement gaps to measure the inter frequency objects and Event A3 for inter-frequency handover. Event A3 provides a handover triggering mechanism based upon relative measurement results, e.g. it can be configured to trigger when the RSRP of a neighbor cell is stronger than the RSRP of special cell

```Mn + Ofn + Ocn – Hys > Mp + Ofp + Ocp + Off           (Trigger Condition)
Mn + Ofn + Ocn + Hys < Mp + Ofp + Ocp + Off           (Cancellation  Condition)
```
- **Mn** is the measurement result of the neighboring cell
- **Mp** is the measurement result of the SpCell
- **Ofn** is the measurement object specific offset of the reference signal of the neighbour cell
- **Ofp** is the measurement object specific offset of the SpCell
- **Ocn** is the cell specific offset of the neighbor cell
- **Ocp** is the cell specific offset of the SpCell
- **Off** is the offset parameter for this event

## Event A4 (Neighbor becomes better than threshold)
Event A4 is triggered when neighbor cell becomes better than defined threshold. This event can be used for handover procedures which does not depend upon the coverage of the serving cell. For example, in load balancing feature take the decision to handover a UE away from the serving cell due to load conditions rather than radio conditions. In this case, the UE only needs to verify that the target cell is better than certain signal level threshold and can provides adequate coverage.

```Mn + Ofn + Ocn – Hys > Thresh                    (Trigger Condition)
Mn + Ofn + Ocn + Hys < Thresh                    (Cancellation  Condition)
```
## Event A5 (SpCell becomes worse than threshold1 and neighbor becomes better than threshold2)
You can think Event A5 is combination of Event A2 and Event A4. This event  is typically used for intra-frequency or inter-frequency handover procedures. After Event A2 is trigger the UE may be configured with measurement gaps and an Event A5 for inter-frequency handover. Event A5 provides a handover triggering mechanism based upon absolute measurement results. It can be used to trigger a time critical handover when a current special cell becomes weak and it is necessary to change towards another cell which may not satisfy the criteria for an event A3 handover.


```(Event Trigger Condition)
Mp + Hys < Thresh1
Mn+ Ofn +Ocn – Hys > Thresh2

(Event Cancellation  Condition)
Mp – Hys > Thresh1
Mn+ Ofn +Ocn + Hys < Thresh2
```

## Event A6 (Neighbour becomes offset better than SCell)
Event A6 is triggered when a neighbor cell becomes better than a secondary cell by an offset. The offset can be either positive or negative. This measurement reporting event is applicable to Carrier Aggregation

```Mn + Ocn – Hys  > Ms + Ocs + Off                  (Trigger Condition)
Mn + Ocn + Hys < Ms + Ocs + Off                   (Cancellation  Condition)
```

## Event B1 (Inter RAT neighbour becomes better than threshold)
Event B1 can be used for inter-RAT handover procedures which does not depend upon the coverage of the serving cell. For example, in load balancing feature take the decision to move a UE away from NR due to load conditions rather than radio conditions. In this case, the UE only needs to verify that the target cell in other RAT (e.g. LTE) is better than certain signal level threshold and can provides adequate coverage.
```Mn + Ofn + Ocn – Hys > Thresh
Mn + Ofn + Ocn + Hys < Thresh
```

## Event B2 (PCell becomes worse than threshold1 and inter RAT neighbor becomes better than threshold2)
Event B2 is triggered when a primary serving cell becomes worse than threshold1, while a neighbor inter-RAT cell becomes better than threshold2. This can be used to trigger inter-RAT mobility procedures when the primary serving cell becomes weak. Inter-system neighbor cell measurements arc used to ensure that the target cell provide.s adequate coverage.

```(Event Trigger Condition)
Mp + Hys < Thresh1
Mn + Ofn + Ocn – Hys > Thresh2

(Event Cancellation  Condition)
Mp – Hys > Thresh1
Mn + Ofn + Ocn + Hys < Thresh2
```

## More detail on measurement
5G NR has introduced cell signal measurement by using SS/PBCH Block (SSB), which is composed of Synchronizations Signal (SS) and Physical Broadcast Channel (PBCH) having longer transmission periodicity than CRS. The number of SSB in one burst depend on the Operating frequency. If Operating frequency (fc) is < 3GHz (FR1) the no. of SSB is 4, for  fc = 3GHz to 6 GHz (FR1) no. of SSB  is 8 and for fc >6 GHz mm-wave no. of SSB is be 64 within one burst.

The SSB periodicity can be configured for each cell in the range of 5,10,20,40,80 or 160 ms. However, mobile device do not need to measure cell signal with periodicity as the SSB and the appropriate measurement periodicity can be configured according to the channel condition. This is desirable and can help to avoid unnecessary measurements and reduce the power consumption on Mobile Device (UE).

3GPP specifications has introduced SSB-based RRM Measurement Timing Configuration window (called SMTC window) shall be notify to Device (UE) regarding the measurement periodicity and timings of SSBs that Device (UE) can use for measurements.

SMTC window periodicity can be set in the same range of SSB i.e. 5, 10, 20, 40, 80 or 160 ms and window duration can be set to 1, 2, 3, 4, or 5 ms, according to the number of SSBs transmitted on the cell being measured. Here we can see that NR cell “A” and NR cell “B” are measured with different window periodicity and different window duration.  When a Device (UE) has been notified of SMTC window by base station, it detects and measure the SSBs within that window and reports the measurement results back to the base station.