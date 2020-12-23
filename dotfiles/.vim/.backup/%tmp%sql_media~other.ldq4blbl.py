Vim�UnDo� ��\��R-��>��Pyx̩i�fmԾ? +�   n                                   _Ve    _�                             ����                                                                                                                                                                                                                                                                                                                                                             _V^     �              n   # -*- coding: utf-8 -*-       	import os   from datetime import datetime   from hashlib import sha256       0from sqlalchemy import Table, ForeignKey, Column   @from sqlalchemy.types import Unicode, Integer, DateTime, Boolean   ,from sqlalchemy.orm import relation, synonym       =from rocket.model import DeclarativeBase, metadata, DBSession   [from rocket.lib.model_utils import PhatBase, common_columns, get_phat_table, get_type_table       E# ********************* Cabinets ***********************************#   XMediaCabinetType = get_type_table(model_name='MediaCabinet', table_name='media_cabinet')       tbl_media_cabinet = {   )    '__tablename__': 'tbl_media_cabinet',   7    'name': common_columns.get('title_not_nullable')(),   D    'description': common_columns.get('description_not_nullable')(),   J    'media_cabinet_type_id': common_columns.get('integer_not_nullable')(),       }   VMediaCabinet = get_phat_table(model_name='MediaCabinet', columndict=tbl_media_cabinet)       tbl_media_cabinet_tag_link = {   2    '__tablename__': 'tbl_media_cabinet_tag_link',   E    'media_cabinet_id': common_columns.get('integer_not_nullable')(),   A    'media_tag_id': common_columns.get('integer_not_nullable')(),       }   mMediaCabinetTagLink = get_phat_table(model_name='MediaCabinetTagLink', columndict=tbl_media_cabinet_tag_link)       tbl_media_cabinet_user_link = {   3    '__tablename__': 'tbl_media_cabinet_role_link',   E    'media_cabinet_id': common_columns.get('integer_not_nullable')(),   <    'user_id': common_columns.get('integer_not_nullable')(),       }   pMediaCabinetUserLink = get_phat_table(model_name='MediaCabinetUserLink', columndict=tbl_media_cabinet_user_link)       C# ********************* Drawer ***********************************#   tbl_media_drawer = {   (    '__tablename__': 'tbl_media_drawer',   E    'media_cabinet_id': common_columns.get('integer_not_nullable')(),   7    'name': common_columns.get('title_not_nullable')(),   D    'description': common_columns.get('description_not_nullable')(),       }   SMediaDrawer = get_phat_table(model_name='MediaDrawer', columndict=tbl_media_drawer)       tbl_media_drawer_tag_link = {   1    '__tablename__': 'tbl_media_drawer_tag_link',   D    'media_drawer_id': common_columns.get('integer_not_nullable')(),   A    'media_tag_id': common_columns.get('integer_not_nullable')(),       }   jMediaDrawerTagLink = get_phat_table(model_name='MediaDrawerTagLink', columndict=tbl_media_drawer_tag_link)       tbl_media_drawer_user_link = {   2    '__tablename__': 'tbl_media_drawer_user_link',   D    'media_drawer_id': common_columns.get('integer_not_nullable')(),   <    'user_id': common_columns.get('integer_not_nullable')(),       }   mMediaDrawerUserLink = get_phat_table(model_name='MediaDrawerUserLink', columndict=tbl_media_drawer_user_link)       A# ********************* File ***********************************#   OMediaFileType = get_type_table(model_name='MediaFile', table_name='media_file')       tbl_media_file = {   &    '__tablename__': 'tbl_media_file',   D    'media_drawer_id': common_columns.get('integer_not_nullable')(),   7    'name': common_columns.get('title_not_nullable')(),   D    'description': common_columns.get('description_not_nullable')(),   G    'media_file_type_id': common_columns.get('integer_not_nullable')(),   >    'location': common_columns.get('longtext_not_nullable')(),   9    'size': common_columns.get('integer_not_nullable')(),   <    'version': common_columns.get('integer_not_nullable')(),       }   MMediaFile = get_phat_table(model_name='MediaFile', columndict=tbl_media_file)       tbl_media_file_version_link = {   3    '__tablename__': 'tbl_media_file_version_link',   F    'new_media_file_id': common_columns.get('integer_not_nullable')(),   K    'previous_media_file_id': common_columns.get('integer_not_nullable')(),       }   pMediaFileVersionLink = get_phat_table(model_name='MediaFileVersionLink', columndict=tbl_media_file_version_link)       #tbl_media_file_download_history = {   7    '__tablename__': 'tbl_media_file_download_history',   B    'media_file_id': common_columns.get('integer_not_nullable')(),   E    'download_user_id': common_columns.get('integer_not_nullable')(),       }   |MediaFileDownloadHistory = get_phat_table(model_name='MediaFileDownloadHistory', columndict=tbl_media_file_download_history)       tbl_media_file_tag_link = {   /    '__tablename__': 'tbl_media_file_tag_link',   B    'media_file_id': common_columns.get('integer_not_nullable')(),   A    'media_tag_id': common_columns.get('integer_not_nullable')(),       }   dMediaFileTagLink = get_phat_table(model_name='MediaFileTagLink', columndict=tbl_media_file_tag_link)       =# ********************* Tag Cloud  ************************ #   tbl_media_tag = {   %    '__tablename__': 'tbl_media_tag',   7    'name': common_columns.get('title_not_nullable')(),       }   JMediaTag = get_phat_table(model_name='MediaTag', columndict=tbl_media_tag)       tbl_media_stop_word = {   +    '__tablename__': 'tbl_media_stop_word',   7    'name': common_columns.get('title_not_nullable')(),       }   ZMediaStopWord = get_phat_table(model_name='MediaStopWord', columndict=tbl_media_stop_word)    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _Vb     �                   �               5�_�                     o        ����                                                                                                                                                                                                                                                                                                                                                             _Vd    �   n   o           5��