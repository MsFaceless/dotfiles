Vim�UnDo� �}�$=����,T�+hh:*L�L8����a  �                 '       '   '   '    ^ X<    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ^ �     �              5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^ �     �              �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^ �     �                #class_name = Entity5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^      �               #table_name = tbl_entity5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^      �               #table_name = tbl_entit5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^      �               #table_name = tbl_enti5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^      �               #table_name = tbl_ent5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             ^      �               #table_name = tbl_en5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             ^      �               #table_name = tbl_e5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             ^      �               #table_name = tbl_5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                         9       v   9    ^      �               `#columns_to_create = [id,entity_type_id,code,register_date] #id - primary_key autoincrement=True5�_�                    
       ����                                                                                                                                                                                                                                                                                                                            
          
   3       v   3    ^      �   	            5#view_cols_list = [entity_type_id,code,register_date]5�_�                           ����                                                                                                                                                                                                                                                                                                                            
          
   3       v   3    ^       �   
            7#search_cols_list = [entity_type_id,code,register_date]5�_�                          ����                                                                                                                                                                                                                                                                                                                            
          
   3       v   3    ^ "     �               4#pdf_cols_list = [entity_type_id,code,register_date]5�_�                           ����                                                                                                                                                                                                                                                                                                                            
          
   3       v   3    ^ �     �               ?#columns_to_create = [id,] #id - primary_key autoincrement=True5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                         W       v   W    ^ �     �   	            #view_cols_list = []�   
          5�_�                           ����                                                                                                                                                                                                                                                                                                                                         W       v   W    ^ �     �   
            #search_cols_list = []�             5�_�                           ����                                                                                                                                                                                                                                                                                                                                         W       v   W    ^ �     �               #pdf_cols_list = []�             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^ �     �                  �               �                #class_name = Entity   #!/bin/python    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ^ �     �            '                order_by(asc($1.id)). \�            '                filter($1.active==1). \�            )            dbase_query = $8.query($1). \�            3            filter(.id==kwargs.get('_id', None)). \�  
                  return .query(). \�   �   �                this = ()�   6   8            Docstring for .�   )   +        class (DeclarativeBase):�            `!p   	snip >> 2   9write_search_dbase_queries(args, snip, t[2], t[1], t[8])`�            `!p   	snip >> 2   args = get_args(t[11])   )write_search_kwarglist(args, snip, t[2])`�            2    def get_active_$2_list(self, *args, **kwargs):�            7            filter($1.id==kwargs.get('$2_id', None)). \�  
                  return $8.query($1). \�  	          ,    def get_$2_by_id(self, *args, **kwargs):�                    $8.flush()�      !      e        if not this: return json.dumps({'success' : False, 'data' : 'No  found for id provided'}) `!p   	snip >> 2   args = get_args(t[5])   +write_save_record_nowui(args, snip, t[2]) `�      !      g        if not this: return json.dumps({'success' : False, 'data' : 'No $2 found for id provided'}) `!p�      !      (        this = self.get_$2_by_id(**data)�   �     !      ,    def save_edit_$2(self, *args, **kwargs):�   �   �  !              $8.flush()�   �   �  !              $8.add(this)�   �   �  $              this = ()`!p   	snip >> 2   args = get_args(t[5])   +write_save_record_nowui(args, snip, t[4]) `�   �   �  $              this = $1()`!p�   �   �  $      +    def save_new_$2(self, *args, **kwargs):�   �   �  $      %        $('#dialog_edit_$2').modal();�   �   �  $      /            $('#dialog_edit_$2').modal('hide');�   �   �  $      '        $('.$2_back').click(function(){�   �   �  $      .                        $.redirect('/$6/$2s');�   �   �  $      A                $.post('/$6/save_edit_$2?', data, function(data){�   �   �  $      >                var formserial = getFormData('#form_edit_$2');�   �   �  $      6             var valid = FormIsValid("#form_edit_$2");�   �   �  $      ,        $('#save_edit_$2').click(function(){�   �   �  (      -        setFormValidation('#form_edit_'); `!p   	snip >> 2   snip.rv = ""   args = get_args(t[5])   &write_datepicker_js(args, snip, t[2])`�   �   �  (      /        setFormValidation('#form_edit_$2'); `!p�   �   �  (      W                        <button class="btn btn-outline-primary $2_back">Cancel</button>�   �   �  (      W                        <button id='save_edit_$2' class="btn btn-primary">Save</button>�   �   �  +      2                        <form id='form_edit_'> `!p   	snip >> 7   args = get_args(t[5])   )write_edit_form_cards(args, snip, t[2]) `�   �   �  +      4                        <form id='form_edit_$2'> `!p�   �   �  +      N                            <h4 class="card-title">New ${2/\w+\s*/\u$0/g}</h4>�   �   �  +              <div class="modal fade" id="dialog_edit_$2" tabindex="-1" role="dialog" aria-labelledby="my$2Label" aria-hidden="true">�   �   �  +      1        this = self.get_$2_by_id(*args, **kwargs)�   �   �  +              if not $2_id: return ''�   �   �  +      )        $2_id = kwargs.get('$2_id', None)�   �   �  +      1    def get_modal_edit_$2(self, *args, **kwargs):�   �   �  +      $        $('#dialog_new_$2').modal();�   �   �  +      .            $('#dialog_new_$2').modal('hide');�   �   �  +      '        $('.$2_back').click(function(){�   �   �  +      .                        $.redirect('/$6/$2s');�   �   �  +      @                $.post('/$6/save_new_$2?', data, function(data){�   �   �  +      =                var formserial = getFormData('#form_new_$2');�   �   �  +      5             var valid = FormIsValid("#form_new_$2");�   �   �  +      +        $('#save_new_$2').click(function(){�   �   �  /      ,        setFormValidation('#form_new_'); `!p   	snip >> 2   snip.rv = ""   args = get_args(t[5])   &write_datepicker_js(args, snip, t[2])`�   �   �  /      .        setFormValidation('#form_new_$2'); `!p�   �   �  /      W                        <button class="btn btn-outline-primary $2_back">Cancel</button>�   �   �  /      V                        <button id='save_new_$2' class="btn btn-primary">Save</button>�   �   �  2      1                        <form id='form_new_'> `!p   	snip >> 8   args = get_args(t[10])   (write_new_form_cards(args, snip, t[2]) `�   �   �  2      3                        <form id='form_new_$2'> `!p�   �   �  2      N                            <h4 class="card-title">New ${2/\w+\s*/\u$0/g}</h4>�   �   �  2      ~        <div class="modal fade" id="dialog_new_$2" tabindex="-1" role="dialog" aria-labelledby="my$2Label" aria-hidden="true">�   �   �  2      0    def get_modal_new_$2(self, *args, **kwargs):�   }     2      Q            $('#dialogdiv').load('/$6/get_modal_edit_$2?'+kwargs, function(data){�   |   ~  2      8            var kwargs = '$2_id='+$(this).attr('$2_id');�   {   }  2      '        $(".$2_edit").click(function(){�   w   y  2      I            $('#dialogdiv').load('/$6/get_modal_new_$2?', function(data){�   v   x  2      -        $("#create_new_$2").click(function(){�   t   v  2      8    def get_javascript_$2_onload(self, *args, **kwargs):�   j   l  2      !                        {$2table}�   Z   \  2                                  <button id="create_new_$2" class="btn btn-primary ml-auto">Create a new ${2/\w+\s*/\u$0/g}</button>�   W   Y  2      J                            <h4 class="card-title">${2/\w+\s*/\u$0/g}</h4>�   O   Q  2      S        $2table = build_html_table(outputlist, dbcolumnlist, theadlist, "$2_table")�   M   O  6              theadlist=[ `!p   	snip >> 4   snip.rv = ""   args = get_args(t[10])   !write_headers(args, snip, t[4]) `�   K   M  :              dbcolumnlist=[ `!p   	snip >> 4   snip.rv = ""   args = get_args(t[10])   #write_dictstuff(args, snip, t[4]) `�   I   K  =      #            outputlist.append({ `!p   	snip >> 4   args = get_args(t[10])   $write_outputlist(args, snip, t[2]) `�   F   H  =      >        dbase_query = self.get_active_$2_list(*args, **kwargs)�   D   F  =      2    def get_active_$2_html(self, *args, **kwargs):�   @   B  =      $        title = "${2/\w+\s*/\u$0/g}"�   ?   A  =      4        javascript = self.get_javascript_$2_onload()�   >   @  =      7        html = self.get_active_$2_html(*args, **kwargs)�   =   ?  =      #    def $2s(self, *args, **kwargs):�   6   8  =      Y    `!p snip.rv = triple_quotes(snip)`Docstring for $6.`!p snip.rv = triple_quotes(snip)`�   5   7  =      class $9(BaseController):�   4   6  =      $0�   *   ,  C          __tablename__=''`!p   snip.rv = ""   	snip >> 1   args = get_args(t[5])   $write_model_column(args, snip, t[4])   if args:   2    snip.rv += '\n' + snip.mkline('', indent='') `�   *   ,  C          __tablename__='$2'`!p�   )   +  C      class $1(DeclarativeBase):�   #   %  C      #link_class_name_None =${14}�   "   $  C      #link_to_id_or_None =${13}�   !   #  C      #pdf_cols_list = [$12]�       "  C      #search_cols_list = [$11]�      !  C      #view_cols_list = [$10]�         C      #controller_name =${9}�        C      #dbsession =${8}�        C      #html_template_name =${7}�        C      #cont_name =${6}�        C      >#columns_to_create = [$5] #id - primary_key autoincrement=True�        C      #postfix =${4}�        C      #prefix =${3}�        C      #table_name =${2}�        C      ##class_name = ${1:GenericClassName}�                 _tgcreateclass_nowui_modal5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ^ �     �            �            5                order_by(asc(GenericClassName.id)). \�            5                filter(GenericClassName.active==1). \�            5            dbase_query = .query(GenericClassName). \�            C            filter(GenericClassName.id==kwargs.get('_id', None)). \�  
          *        return .query(GenericClassName). \�   �   �        !        this = GenericClassName()�   )   +        (class GenericClassName(DeclarativeBase):�              #class_name = GenericClassName5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ^ �     �            %                order_by(asc(.id)). \�            %                filter(.active==1). \�            %            dbase_query = .query(). \�            3            filter(.id==kwargs.get('_id', None)). \�  
                  return .query(). \�   �   �                this = ()�   )   +        class (DeclarativeBase):�              #class_name = �            5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ^ �     �            0    def get_active__list(self, *args, **kwargs):�            ?            filter(Organisation.id==kwargs.get('_id', None)). \�  	          *    def get__by_id(self, *args, **kwargs):�            b        if not this: return json.dumps({'success' : False, 'data' : 'No  found for id provided'}) �            &        this = self.get__by_id(**data)�   �           *    def save_edit_(self, *args, **kwargs):�   �   �        )    def save_new_(self, *args, **kwargs):�   �   �        #        $('#dialog_edit_').modal();�   �   �        -            $('#dialog_edit_').modal('hide');�   �   �        %        $('._back').click(function(){�   �   �        *                        $.redirect('//s');�   �   �        =                $.post('//save_edit_?', data, function(data){�   �   �        <                var formserial = getFormData('#form_edit_');�   �   �        4             var valid = FormIsValid("#form_edit_");�   �   �        *        $('#save_edit_').click(function(){�   �   �        *        setFormValidation('#form_edit_'); �   �   �        U                        <button class="btn btn-outline-primary _back">Cancel</button>�   �   �        U                        <button id='save_edit_' class="btn btn-primary">Save</button>�   �   �        /                        <form id='form_edit_'> �   �   �        <                            <h4 class="card-title">New </h4>�   �   �        {        <div class="modal fade" id="dialog_edit_" tabindex="-1" role="dialog" aria-labelledby="myLabel" aria-hidden="true">�   �   �        /        this = self.get__by_id(*args, **kwargs)�   �   �                if not _id: return ''�   �   �        %        _id = kwargs.get('_id', None)�   �   �        /    def get_modal_edit_(self, *args, **kwargs):�   �   �        "        $('#dialog_new_').modal();�   �   �        ,            $('#dialog_new_').modal('hide');�   �   �        %        $('._back').click(function(){�   �   �        *                        $.redirect('//s');�   �   �        <                $.post('//save_new_?', data, function(data){�   �   �        ;                var formserial = getFormData('#form_new_');�   �   �        3             var valid = FormIsValid("#form_new_");�   �   �        )        $('#save_new_').click(function(){�   �   �        )        setFormValidation('#form_new_'); �   �   �        U                        <button class="btn btn-outline-primary _back">Cancel</button>�   �   �        T                        <button id='save_new_' class="btn btn-primary">Save</button>�   �   �        .                        <form id='form_new_'> �   �   �        <                            <h4 class="card-title">New </h4>�   �   �        z        <div class="modal fade" id="dialog_new_" tabindex="-1" role="dialog" aria-labelledby="myLabel" aria-hidden="true">�   �   �        .    def get_modal_new_(self, *args, **kwargs):�   }           M            $('#dialogdiv').load('//get_modal_edit_?'+kwargs, function(data){�   |   ~        4            var kwargs = '_id='+$(this).attr('_id');�   {   }        %        $("._edit").click(function(){�   w   y        E            $('#dialogdiv').load('//get_modal_new_?', function(data){�   v   x        +        $("#create_new_").click(function(){�   t   v        6    def get_javascript__onload(self, *args, **kwargs):�   j   l                                {table}�   Z   \        k                            <button id="create_new_" class="btn btn-primary ml-auto">Create a new </button>�   W   Y        8                            <h4 class="card-title"></h4>�   O   Q        O        table = build_html_table(outputlist, dbcolumnlist, theadlist, "_table")�   F   H        <        dbase_query = self.get_active__list(*args, **kwargs)�   D   F        0    def get_active__html(self, *args, **kwargs):�   @   B                title = ""�   ?   A        2        javascript = self.get_javascript__onload()�   >   @        5        html = self.get_active__html(*args, **kwargs)�   =   ?        !    def s(self, *args, **kwargs):�   *   ,            __tablename__=''�              #table_name =�            5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ^ �     �              	#prefix =�            5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                v       ^ �     �              
#postfix =�            5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ^ �     �  5  ;  K      r        if not this: return json.dumps({'success' : False, 'data' : 'No tbl_organisation found for id provided'}) �  $  *  G              this = Organisation()�   �   �        ?                        <form id='form_edit_tbl_organisation'> �   *   2        $    __tablename__='tbl_organisation'�              <#columns_to_create = [] #id - primary_key autoincrement=True�            5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ^ �     �      O      :                        $.redirect('//tbl_organisations');�      O      M                $.post('//save_edit_tbl_organisation?', data, function(data){�   �   �  O      :                        $.redirect('//tbl_organisations');�   �   �  O      L                $.post('//save_new_tbl_organisation?', data, function(data){�   �   �  O      ]            $('#dialogdiv').load('//get_modal_edit_tbl_organisation?'+kwargs, function(data){�   }     O      U            $('#dialogdiv').load('//get_modal_new_tbl_organisation?', function(data){�   <   >  O          """Docstring for ."""�        O      #cont_name =�        O    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ^ �     �        O      #html_template_name =�        O    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ^ �     �  J  L  O      1            dbase_query = .query(Organisation). \�  @  B  O      &        return .query(Organisation). \�  ;  =  O              .flush()�  ,  .  O              .flush()�  +  -  O              .add(this)�        O      #dbsession =�        O    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       ^ �     �   ;   =  O      class (BaseController):�         O      #controller_name =�         O    5�_�      !                       ����                                                                                                                                                                                                                                                                                                                                                v       ^ �     �   �   �  [      >                        <form id='form_new_tbl_organisation'> �   [   a  W              theadlist=[ �   U   [  S              dbcolumnlist=[ �   O   U  O                   outputlist.append({ �      !  O      #view_cols_list = []�       !  O    5�_�       "           !   !       ����                                                                                                                                                                                                                                                                                                                                                v       ^ �     �  x  �         �  s  y  {       �       "  {      #search_cols_list = []�   !   "  {    5�_�   !   #           "   "       ����                                                                                                                                                                                                                                                                                                                                                v       ^ �     �   !   #  �      #pdf_cols_list = []�   "   #  �    5�_�   "   $           #   &        ����                                                                                                                                                                                                                                                                                                                            6           &           V        ^ �    �   %   &          ############################   # Model   ############################       $class Organisation(DeclarativeBase):   $    __tablename__='tbl_organisation'   >    id = Column(Integer, autoincrement=True, primary_key=True)        name = Column(Unicode(255))    &    tax_number = Column(Unicode(255))    /    registration_number = Column(Unicode(255))    7    financial_regulatory_number = Column(Unicode(255))        *    active = Column(Boolean, default=True)   .    added_by = Column(Integer, nullable=False)   2    added = Column(DateTime, default=datetime.now)   :    tenant_id = Column(Integer, default=1, nullable=False)    5�_�   #   %           $   ?        ����                                                                                                                                                                                                                                                                                                                                                             ^ 	�     �  {  }          I            searchphrase = "%"+kwargs['financial_regulatory_number']+"%" �  u  w          A            searchphrase = "%"+kwargs['registration_number']+"%" �  o  q          8            searchphrase = "%"+kwargs['tax_number']+"%" �  i  k          2            searchphrase = "%"+kwargs['name']+"%" �  P  R          r        if not this: return json.dumps({'success' : False, 'data' : 'No tbl_organisation found for id provided'}) �  "  $          :        setFormValidation('#form_edit_tbl_organisation'); �   �   �          ?                        <form id='form_edit_tbl_organisation'> �   �   �          9        setFormValidation('#form_new_tbl_organisation'); �   �   �          >                        <form id='form_new_tbl_organisation'> �   N   P          /                'Financial_Regulatory_Number', �   M   O          '                'Registration_Number', �   L   N                          'Tax_Number', �   K   M                          'Name', �   J   L                  theadlist=[ �   H   J          /                'financial_regulatory_number', �   G   I          '                'registration_number', �   F   H                          'tax_number', �   E   G                          'name', �   D   F                  dbcolumnlist=[ �   B   D          R                'financial_regulatory_number' : item.financial_regulatory_number, �   A   C          B                'registration_number' : item.registration_number, �   @   B          0                'tax_number' : item.tax_number, �   ?   A          �                'name' : "<div class='edit tbl_organisation_edit' tbl_organisation_id='{1}'>{0}</div>".format(item.name, item.id),  �   >   @                       outputlist.append({ 5�_�   $   &           %           ����                                                                                                                                                                                                                                                                                                                                                             ^ 	�     �   !   #          R#pdf_cols_list = [name,tax_number,registration_number,financial_regulatory_number]�       "          U#search_cols_list = [name,tax_number,registration_number,financial_regulatory_number]�      !          S#view_cols_list = [name,tax_number,registration_number,financial_regulatory_number]�                ~#columns_to_create = [id,name,tax_number,registration_number,financial_regulatory_number] #id - primary_key autoincrement=True�                R#pdf_cols_list = [name,tax_number,registration_number,financial_regulatory_number]�   
             U#search_cols_list = [name,tax_number,registration_number,financial_regulatory_number]�   	             S#view_cols_list = [name,tax_number,registration_number,financial_regulatory_number]�                ~#columns_to_create = [id,name,tax_number,registration_number,financial_regulatory_number] #id - primary_key autoincrement=True5�_�   %   '           &           ����                                                                                                                                                                                                                                                                                                                                                             ^ 	�    �   �   �          G                            <div style='display:none' class="col-md-6">�                /@r: 16ggf:wv$"qy 17ggf:wv$"wy 18ggf:wv$"ty @q@t5�_�   &               '  F       ����                                                                                                                                                                                                                                                                                                                                                             ^ X;    �  E  F          *        this.tenant_id = usernow.tenant_id5�_�                           ����                                                                                                                                                                                                                                                                                                                            
          
   3       v   3    ^ !     �               .#pdf_cols_list = [en#link_to_id_or_None = None5��