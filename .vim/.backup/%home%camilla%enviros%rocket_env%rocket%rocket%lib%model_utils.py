Vim�UnDo� T��ɼ��q�1}�KM���\���.Hp�F�   �   .    added_by = common_columns.get('integer')()   <   *      @       @   @   @    ^&�C    _�                     �        ����                                                                                                                                                                                                                                                                                                                            9          �   *       V       ^d     �   �  .   �    �   �   �   �    5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            9          �   *       V       ^e     �   �   �  F    5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �          �   	       v   	    ^j     �   �   �  G      class PhatBase(object):5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �          �   	       v   	    ^j     �   �   �  G      class Base(object):5�_�                    �   *    ����                                                                                                                                                                                                                                                                                                                            �          �   	       v   	    ^o     �   �   �  G      .    added_by = common_columns.get('integer')()5�_�                    �   5    ����                                                                                                                                                                                                                                                                                                                            �          �   	       v   	    ^q     �   �   �  G      6    added_by = common_columns.get('integer_default')()5�_�      	              �       ����                                                                                                                                                                                                                                                                                                                            �          �   	       v   	    ^v     �   �   �          +                filter(cls.active==True). \5�_�      
          	   �       ����                                                                                                                                                                                                                                                                                                                            �          �   	       v   	    ^y     �   �   �          +                filter(cls.active==True). \5�_�   	              
   �       ����                                                                                                                                                                                                                                                                                                                            �          �   %       v   %    ^|     �   �   �  E      (    def get_all(cls, attr, active=True):5�_�   
                 �       ����                                                                                                                                                                                                                                                                                                                            �          �   %       v   %    ^}     �   �   �          -                filter(cls.active==active). \5�_�                   �   "    ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �   �   �  D      1    def get_limit(cls, limit, attr, active=True):5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �   �   �          -                filter(cls.active==active). \5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �   �   �          +                filter(cls.active==True). \5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �   �   �          +                filter(cls.active==True). \5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �   �   �          +                filter(cls.active==True). \5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �   �   �          +                filter(cls.active==True). \5�_�                          ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �              +                filter(cls.active==True). \5�_�                   
       ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �  	  
          +                filter(cls.active==True). \5�_�                          ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �              +                filter(cls.active==True). \5�_�                          ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �              +                filter(cls.active==True). \5�_�                          ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �              +                filter(cls.active==True). \5�_�                   3   #    ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �  2  4  :      O    type_table = type(model_name, (PhatBase, DeclarativeBase), type_table_dict)5�_�                   3   #    ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �  2  4  :      N    type_table = type(model_name, (hatBase, DeclarativeBase), type_table_dict)5�_�                   3   #    ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �  2  4  :      M    type_table = type(model_name, (atBase, DeclarativeBase), type_table_dict)5�_�                   3   #    ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �  2  4  :      L    type_table = type(model_name, (tBase, DeclarativeBase), type_table_dict)5�_�                   3   #    ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�    �  2  4  :      K    type_table = type(model_name, (Base, DeclarativeBase), type_table_dict)5�_�                            ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�     �                     return Column(Numeric(22,8))5�_�                             ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�    �  /  1                      'name':name,�  .  0                      'id':primary_id,�  -  /          &            '__tablename__':tablename,�   �   �          ?        return f"<{self.id}: {self.__tablename__[4:].title()}>"�   @   B          ?        return f"<{self.id}: {self.__tablename__[4:].title()}>"�   1   3          $print("Current common_columns are:")�   (   *          :        'currency':common_numeric_columns.get('currency'),�   '   )                  'date':get_date_column,�   &   (                  'time':get_time_column,�   %   '          '        'datetime':get_datetime_column,�   $   &          %        'boolean':get_boolean_column,�   #   %          %        'numeric':get_numeric_column,�   !   #          :        'longtext':common_unicode_columns.get('longtext'),�       "          4        'title':common_unicode_columns.get('title'),�      !          @        'description':common_unicode_columns.get('description'),5�_�                     �       ����                                                                                                                                                                                                                                                                                                                            �   "       �   .       v   .    ^�    �   �   �  ;              �   �   �  :    5�_�      !               �        ����                                                                                                                                                                                                                                                                                                                            �           �           V       ^�     �   �   �                  @classmethod       def latest_entry(cls):   &        return DBSession.query(cls). \   -                order_by(cls.added.desc()). \                   first()           @classmethod       def oldest_entry(cls):   &        return DBSession.query(cls). \   ,                order_by(cls.added.asc()). \                   first()    5�_�       "           !   �       ����                                                                                                                                                                                                                                                                                                                            �           �           V       ^�     �   �   �  .    5�_�   !   #           "   �        ����                                                                                                                                                                                                                                                                                                                            �           �          V       ^�     �   �   �                  @classmethod   $    def get_limit(cls, limit, attr):   &        return DBSession.query(cls). \   4                order_by(asc(getattr(cls, attr))). \                   limit(limit)           @classmethod   (    def by_attr_count(cls, attr, value):   &        return DBSession.query(cls). \   4                filter(getattr(cls, attr)==value). \                   count()           @classmethod   &    def by_attr_one(cls, attr, value):   &        return DBSession.query(cls). \   4                filter(getattr(cls, attr)==value). \                   one()5�_�   "   $           #   �        ����                                                                                                                                                                                                                                                                                                                            �           �           V        ^�     �   �   �                  @classmethod   &    def by_attr_all(cls, attr, value):   &        return DBSession.query(cls). \   4                filter(getattr(cls, attr)==value). \                   all()           @classmethod   /    def by_attr_limit(cls, attr, value, limit):   &        return DBSession.query(cls). \   4                filter(getattr(cls, attr)==value). \                   limit(limit)           @classmethod   /    def like_attr_one(cls, attr, value, limit):   &        return DBSession.query(cls). \   9                filter(getattr(cls, attr).like(value)). \                   one()           @classmethod   1    def like_attr_first(cls, attr, value, limit):   &        return DBSession.query(cls). \   9                filter(getattr(cls, attr).like(value)). \                   first()5�_�   #   &           $   �        ����                                                                                                                                                                                                                                                                                                                            �           �           V        ^�    �   �   �                  @classmethod   /    def like_attr_all(cls, attr, value, limit):   &        return DBSession.query(cls). \   9                filter(getattr(cls, attr).like(value)). \                   all()           @classmethod   1    def like_attr_limit(cls, attr, value, limit):   &        return DBSession.query(cls). \   9                filter(getattr(cls, attr).like(value)). \                   limit(limit)           @classmethod       def by_id(cls, id):   *        return cls.by_attr_first('id', id)5�_�   $   (   %       &   �       ����                                                                                                                                                                                                                                                                                                                            �           �           V        ^�     �   �   �   �      O    type_table = type(model_name, (TypeBase, DeclarativeBase), type_table_dict)5�_�   &   )   '       (   �        ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^     �   �   �          0    tablename = f'tbl_{table_name.lower()}_type'5�_�   (   *           )   �        ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^     �   �   �          '            '__tablename__': tablename,5�_�   )   +           *   �        ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^     �   �   �          #    modelname = f'{model_name}Type'5�_�   *   /           +   �        ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^    �   �   �          N    type_table = type(modelname, (TypeBase, DeclarativeBase), type_table_dict)5�_�   +   7   ,       /   �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^�   
 �   �   �   �              print(cls, attr)5�_�   /   8   6       7   �       ����                                                                                                                                                                                                                                                                                                                            �   #       A   "       v   "    ^�     �   �   �          #        print(cls, attr, DBSession)5�_�   7   9           8   �   #    ����                                                                                                                                                                                                                                                                                                                            �   #       �   <       v   <    ^�     �   �   �   �      @        return f"<{self.id}: {self.__tablename__[4: ].title()}>"5�_�   8   :           9   �   #    ����                                                                                                                                                                                                                                                                                                                            �   #       �   <       v   <    ^�    �   �   �   �      &        return f"<{self.id}: {self.}>"5�_�   9   ;           :   1        ����                                                                                                                                                                                                                                                                                                                                                             ^!��     �   0   2   �      print("*"*80)5�_�   :   <           ;   2        ����                                                                                                                                                                                                                                                                                                                                                             ^!��     �   1   3   �      %print("Current common_columns are: ")5�_�   ;   =           <   3        ����                                                                                                                                                                                                                                                                                                                                                             ^!��     �   2   4   �      print("*"*80)5�_�   <   >           =   4        ����                                                                                                                                                                                                                                                                                                                                                             ^!��     �   3   5   �      !for key in common_columns.keys():5�_�   =   ?           >   5        ����                                                                                                                                                                                                                                                                                                                                                             ^!��     �   4   6   �          print(key)5�_�   >   @           ?   6        ����                                                                                                                                                                                                                                                                                                                                                             ^!��    �   5   7   �      print("*"*80)5�_�   ?               @   <   *    ����                                                                                                                                                                                                                                                                                                                                                             ^&�C    �   ;   =   �      .    added_by = common_columns.get('integer')()5�_�   /       0   7   6   �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^     �   �   �        5�_�   /   1       6   0   �   "    ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^�    �   �   �   �      %        print(cls, attr, DBSession())5�_�   0   2           1   �   #    ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^�     �   �   �   �              �   �   �   �              session = DBSession()5�_�   1   3           2   �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^     �   �   �   �      %        return BSession.query(cls). \5�_�   2   4           3   �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^     �   �   �   �      $        return Session.query(cls). \5�_�   3   5           4   �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^     �   �   �   �      #        return ession.query(cls). \5�_�   4               5   �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^   	 �   �   �   �      $        return session.query(cls). \5�_�   +   -       /   ,   �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^�     �   �   �   �              �   �   �   �              DBSession()5�_�   ,   .           -   �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^�     �   �   �   �      (        return DBSession().query(cls). \5�_�   -               .   �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       ^�    �   �   �        5�_�   &           (   '   �       ����                                                                                                                                                                                                                                                                                                                            �           �           V        ^�     �   �   �   �      5    tablename_type = f'tbl_{table_name.lower()}_type'5�_�   $           &   %   �       ����                                                                                                                                                                                                                                                                                                                            �           �           V        ^�     �   �   �   �      N    type_table = type(modelname, (TypeBase, DeclarativeBase), type_table_dict)5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �          �   %       v   %    ^�     �   �   �        5�_�              	      �       ����                                                                                                                                                                                                                                                                                                                            �          �   	       v   	    ^x     �   �   �        5��