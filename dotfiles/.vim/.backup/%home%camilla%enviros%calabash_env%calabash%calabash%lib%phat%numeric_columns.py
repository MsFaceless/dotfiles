Vim�UnDo� Ɓv�_o��� ݶ�Y�BF��i)�FI#�s�   �                  0       0   0   0    _tT�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   ^   `          &def col_factor_unique_not_nullable(): �   V   X          3def col_factor_default_not_nullable(default=None): �   P   R          &def col_factor_default(default=None): �   I   K          *def col_percentage_unique_not_nullable(): �   A   C          7def col_percentage_default_not_nullable(default=None): �   ;   =          *def col_percentage_default(default=None): �   3   5          (def col_geocoord_unique_not_nullable(): �   +   -          5def col_geocoord_default_not_nullable(default=None): �   %   '          (def col_geocoord_default(default=None): �                5def col_currency_default_not_nullable(default=None): �                (def col_currency_default(default=None): �                Kdef col_numeric_not_nullable(precision=None, scale=None, extra_params={}): 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �                +    extra_params.update({'nullable':False})5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �                bdef col_currency_unique(): return col_numeric(precision=22, scale=8, extra_params={'unique':True})5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �                |def col_currency_unique_not_nullable(): return col_numeric_not_nullable(precision=22, scale=8, extra_params={'unique':True})5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �                &    extra_params = {'default':default}5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �      !          &    extra_params = {'default':default}5�_�                    )        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   (   *          &    extra_params = {'default':default}5�_�      	              /        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   .   0          &    extra_params = {'default':default}5�_�      
           	   2        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   1   3          bdef col_geocoord_unique(): return col_numeric(precision=10, scale=7, extra_params={'unique':True})5�_�   	              
   5        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   4   6          "    extra_params = {'unique':True}5�_�   
                 ?        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   >   @          &    extra_params = {'default':default}5�_�                    E        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   D   F          &    extra_params = {'default':default}5�_�                    H        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   G   I          cdef col_percentage_unique(): return col_numeric(precision=5, scale=2, extra_params={'unique':True})5�_�                    K        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   J   L          "    extra_params = {'unique':True}5�_�                    T        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   S   U          &    extra_params = {'default':default}5�_�                    Z        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   Y   [          &    extra_params = {'default':default}5�_�                    ]        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   \   ^          _def col_factor_unique(): return col_numeric(precision=8, scale=4, extra_params={'unique':True})5�_�                    `        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   _   a          "    extra_params = {'unique':True}5�_�                    d        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   c   e              'numeric':col_currency,5�_�                    e        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   d   f          5    'numeric_not_nullable':col_currency_not_nullable,5�_�                    f        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   e   g          )    'numeric_unique':col_currency_unique,5�_�                    g        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   f   h          C    'numeric_unique_not_nullable':col_currency_unique_not_nullable,5�_�                    h        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   g   i          +    'numeric_default':col_currency_default,5�_�                    i        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   h   j          E    'numeric_default_not_nullable':col_currency_default_not_nullable,5�_�                    k        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   j   l              'currency':col_currency,5�_�                    l        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   k   m          6    'currency_not_nullable':col_currency_not_nullable,5�_�                    m        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   l   n          *    'currency_unique':col_currency_unique,5�_�                    n        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   m   o          D    'currency_unique_not_nullable':col_currency_unique_not_nullable,5�_�                    o        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   n   p          ,    'currency_default':col_currency_default,5�_�                    p        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   o   q          F    'currency_default_not_nullable':col_currency_default_not_nullable,5�_�                     r        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   q   s              'geocoord':col_geocoord,5�_�      !               s        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   r   t          6    'geocoord_not_nullable':col_geocoord_not_nullable,5�_�       "           !   t        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   s   u          *    'geocoord_unique':col_geocoord_unique,5�_�   !   #           "   u        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   t   v          D    'geocoord_unique_not_nullable':col_geocoord_unique_not_nullable,5�_�   "   $           #   v        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   u   w          ,    'geocoord_default':col_geocoord_default,5�_�   #   %           $   w        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   v   x          F    'geocoord_default_not_nullable':col_geocoord_default_not_nullable,5�_�   $   &           %   y        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   x   z               'percentage':col_percentage,5�_�   %   '           &   z        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   y   {          :    'percentage_not_nullable':col_percentage_not_nullable,5�_�   &   (           '   {        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   z   |          .    'percentage_unique':col_percentage_unique,5�_�   '   )           (   |        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   {   }          H    'percentage_unique_not_nullable':col_percentage_unique_not_nullable,5�_�   (   *           )   }        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   |   ~          0    'percentage_default':col_percentage_default,5�_�   )   +           *   ~        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   }             J    'percentage_default_not_nullable':col_percentage_default_not_nullable,5�_�   *   ,           +   �        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �      �              'factor':col_factor,5�_�   +   -           ,   �        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   �   �          2    'factor_not_nullable':col_factor_not_nullable,5�_�   ,   .           -   �        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   �   �          &    'factor_unique':col_factor_unique,5�_�   -   /           .   �        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   �   �          @    'factor_unique_not_nullable':col_factor_unique_not_nullable,5�_�   .   0           /   �        ����                                                                                                                                                                                                                                                                                                                                                             _tT�     �   �   �          (    'factor_default':col_factor_default,5�_�   /               0   �        ����                                                                                                                                                                                                                                                                                                                                                             _tT�    �   �   �          B    'factor_default_not_nullable':col_factor_default_not_nullable,5��