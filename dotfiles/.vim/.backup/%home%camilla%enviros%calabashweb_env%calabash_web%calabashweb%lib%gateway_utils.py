Vim�UnDo� �?��B�� �j�y�^�(����bp�h	-�                                       _7�    _�                             ����                                                                                                                                                                                                                                                                                                                                                  V        ^�]     �                    "def get_user_profile(params=None):   2    return post_to_url('get_user_profile', params)       &def get_entity_by_mobile(params=None):       print(params)   6    return post_to_url('get_entity_by_mobile', params)       +def get_person_identity_types(params=None):   ;    return post_to_url('get_person_identity_types', params)    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^�^     �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ^�`     �                def update_student(params=None):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ^�`     �               def (params=None):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ^�d     �                    print('params', params)5�_�                           ����                                                                                                                                                                                                                                                                                                                                         ,       v   ,    ^�g     �               7    return post_to_url('update_eiffel_student', params)5�_�                           ����                                                                                                                                                                                                                                                                                                                                         ,       v   ,    ^�g     �               "    return post_to_url('', params)5�_�      	              
   %    ����                                                                                                                                                                                                                                                                                                                                       
   %       V   (    ^�j    �   	   
          %def preregister_student(params=None):   '    print('Gateway URL; ', GATEWAY_URL)   5    return post_to_url('preregister_student', params)    5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             _7�     �      
       �      	       5�_�   	              
   	       ����                                                                                                                                                                                                                                                                                                                            	          	   
       v   
    _7�     �      
         /GATEWAY_URL = env_vars.get('GATEWAY_URL', None)5�_�   
                 	       ����                                                                                                                                                                                                                                                                                                                            	          	   
       v   
    _7�     �      
         ,GATEWAY_ = env_vars.get('GATEWAY_URL', None)5�_�                    	   %    ����                                                                                                                                                                                                                                                                                                                            	   %       	   '       v   '    _7�     �      
         0GATEWAY_GUID = env_vars.get('GATEWAY_URL', None)5�_�                    	   %    ����                                                                                                                                                                                                                                                                                                                            	   %       	   '       v   '    _7�     �      
         -GATEWAY_GUID = env_vars.get('GATEWAY_', None)5�_�                           ����                                                                                                                                                                                                                                                                                                                            	   %       	   '       v   '    _7�     �                   �             5�_�                            ����                                                                                                                                                                                                                                                                                                                            	   %       	   '       v   '    _7�     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                            	   %       	   '       v   '    _7�     �                5�_�                           ����                                                                                                                                                                                                                                                                                                                            	   %       	   '       v   '    _7�     �                   headers = {}5�_�                           ����                                                                                                                                                                                                                                                                                                                            	   %       	   '       v   '    _7�     �                           }5�_�                           ����                                                                                                                                                                                                                                                                                                                            	   %       	   '       v   '    _7�     �               	        }5�_�                            ����                                                                                                                                                                                                                                                                                                                            	   %       	   '       v   '    _7�    �                5�_�                       ?    ����                                                                                                                                                                                                                                                                                                                            	   %       	   '       v   '    _7�     �               @        r = requests.post(f"{GATEWAY_URL}/{url}", params=params)5�_�                            ����                                                                                                                                                                                                                                                                                                                            	   %       	   '       v   '    _7�    �                   �             5�_�                            ����                                                                                                                                                                                                                                                                                                                            	   %       	   '       v   '    _7�     �                5��