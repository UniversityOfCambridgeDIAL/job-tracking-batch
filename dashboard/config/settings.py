# My Settings - default
LOC_FIELDS_SHOWN = ['id','batch','time','user1']
LOC_FIELD_NAMES = {
            'id':'Job Number',
            'batch':'Type',
            'time':'Time',
            'user1':'Comment',
        }

JOB_FIELDS_SHOWN = ['id','batch','location','time','user1']
JOB_FIELD_NAMES = {
            'id':'Job Number',
            'batch':'Type',
            'location':'Locations',
            'time':'Time',
            'user1':'Comment',
        }


SORT_ORDER_DESCENDING = False
SHOW_DURATION = False

ID_AS_LINK = False
LINK_TEMPLATE = 'function get_link_href(id,location){ return "file://///dssiserv03/pgms4factory/JobData/"+location+"/"+id.substring(4)+".pdf" }'

