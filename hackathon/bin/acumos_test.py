from acumos.modeling import Model, List, Dict, create_namedtuple, create_dataframe
from acumos.session import AcumosSession

# replace these fake APIs with ones appropriate for your instance!
session = AcumosSession(push_api="https://my.acumos.instance.com/upload",
                        auth_api="https://my.acumos.instance.com/auth")