# fb-kpimon-xapp
key performance indicator app

This app subscribes to the kpm (key performance metrics) service model and exposes the metrics via a prometheus gauge endpoint.



## Building blocks
- it creates subscriptions based on Kpm service model report styles (KpmReportStyle)
    - defining a List of Action
        - type: ACTION_TYPE_REPORT
        - subsequent_action: sth!
        - payload: action_def
            - E2SmKpmActionDefinition
                - action_definition_format1
                    - cell_obj_id
                    - meas_info_list
                        - report_style.measurements
                    - granul_period
    - defining trigger: E2SmKpmEventTriggerDefinition
        - reporting_period
- then it parses (header, message) recieved from subscription and sets values in the CUSTOM_COLLECTOR.metrics correspondingly!
- 