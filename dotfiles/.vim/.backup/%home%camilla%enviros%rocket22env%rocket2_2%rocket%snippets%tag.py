Vim�UnDo� ��D����U5C;�7�������&V���=��W   �   #pdf_cols_list = []   "                          _V     _�                             ����                                                                                                                                                                                                                                                                                                                                                             _V     �   �   �          ,            this = Cabinet.by_id(cabinet_id)�   �   �                      this = Cabinet()�   �   �          c						<label class="col-md-3 col-form-label" required for="cabinet_type_id">Cabinet_Type_Id</label>�   �   �          C                            <h4 class="card-title">New Cabinet</h4>�   �   �          /            cabinet = Cabinet.by_id(cabinet_id)�   W   Y          w                            <button id="create_new_cabinet" class="btn btn-primary ml-auto">Create New Cabinet</button>�   T   V          ?                            <h4 class="card-title">Cabinet</h4>�   J   L          "                'Cabinet_Type_Id',�   :   <          +        dbase_query = Cabinet.get_all('id')�   5   7                  title = "Cabinet"�                #class_name = Cabinet�                 #class_name = Cabinet5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _V     �   �   �          F            this.cabinet_type_id = kwargs.get('cabinet_type_id', None)�   �   �          (            this = Tag.by_id(cabinet_id)�   �   �          F            this.cabinet_type_id = kwargs.get('cabinet_type_id', None)�   �   �                  if not cabinet_id:�   �   �          3        cabinet_id = kwargs.get('cabinet_id', None)�   �   �          ,    def save_cabinet(self, *args, **kwargs):�   �   �          %        $('#dialog_cabinet').modal();�   �   �          /            $('#dialog_cabinet').modal('hide');�   �   �          ,        $('.cabinet_back').click(function(){�   �   �          2                    $.redirect('/media/cabinets');�   �   �          J                $.post('/media/save_cabinet?', formserial, function(data){�   �   �          ,        $('#save_cabinet').click(function(){�   �   �          %        var form_id = '#form_cabinet'�   �   �          \                        <button class="btn btn-outline-primary cabinet_back">Cancel</button>�   �   �          W                        <button id='save_cabinet' class="btn btn-primary">Save</button>�   �   �          �							<input id="cabinet_type_id" value="{cabinet_type_id}" type="text" name="cabinet_type_id" class="form-control" required='true'>�   �   �          _						<label class="col-md-3 col-form-label" required for="cabinet_type_id">Tag_Type_Id</label>�   �   �          0                        <form id='form_cabinet'>�   �   �          �        <div class="modal fade" id="dialog_cabinet" tabindex="-1" role="dialog" aria-labelledby="mycabinetLabel" aria-hidden="true">�   �   �          D        cabinet_type_id = cabinet.cabinet_type_id if cabinet else ''�   �   �          <        description = cabinet.description if cabinet else ''�   �   �          .        name = cabinet.name if cabinet else ''�   �   �          X            hidden_input = get_hidden_input(**{'id': 'cabinet_id', 'value': cabinet_id})�   �   �          +            cabinet = Tag.by_id(cabinet_id)�   �   �                  if cabinet_id:�   �   �                  cabinet = None�   �   �          3        cabinet_id = kwargs.get('cabinet_id', None)�   �   �          1    def get_modal_cabinet(self, *args, **kwargs):�   z   |          U            $('#dialogdiv').load('/media/get_modal_cabinet?', kwargs, function(data){�   y   {          B            var kwargs = 'cabinet_id='+$(this).attr('cabinet_id');�   x   z          ,        $(".cabinet_edit").click(function(){�   t   v          M            $('#dialogdiv').load('/media/get_modal_cabinet?', function(data){�   s   u          2        $("#create_new_cabinet").click(function(){�   q   s          =    def get_javascript_cabinet_onload(self, *args, **kwargs):�   W   Y          s                            <button id="create_new_cabinet" class="btn btn-primary ml-auto">Create New Tag</button>�   L   N          X        htmltbl = build_html_table(outputlist, dbcolumnlist, theadlist, "cabinet_table")�   E   G          "                'cabinet_type_id',�   @   B          9                'cabinet_type_id' : item.cabinet_type_id,�   >   @          p                'name' : "<div class='edit cabinet_edit' cabinet_id='{1}'>{0}</div>".format(item.name, item.id),�   9   ;          7    def get_active_cabinet_html(self, *args, **kwargs):�   4   6          9        javascript = self.get_javascript_cabinet_onload()�   3   5          <        html = self.get_active_cabinet_html(*args, **kwargs)�   2   4          (    def cabinets(self, *args, **kwargs):�   !   #          5#pdf_cols_list = [name, description, cabinet_type_id]�       "          8#search_cols_list = [name, description, cabinet_type_id]�      !          6#view_cols_list = [name, description, cabinet_type_id]�                b#columns_to_create = [id, name, description, cabinet_type_id] #id - primary_key autoincrement=True�                #table_name =cabinet�                5#pdf_cols_list = [name, description, cabinet_type_id]�   
             8#search_cols_list = [name, description, cabinet_type_id]�   	             6#view_cols_list = [name, description, cabinet_type_id]�                b#columns_to_create = [id, name, description, cabinet_type_id] #id - primary_key autoincrement=True�                #table_name = cabinet5�_�                           ����                                                                                                                                                                                                                                                                                                                                         7       v   7    _V     �         �      ^#columns_to_create = [id, name, description, tag_type_id] #id - primary_key autoincrement=True5�_�                   
   $    ����                                                                                                                                                                                                                                                                                                                            
   $       
   0       v   0    _V     �   	      �      2#view_cols_list = [name, description, tag_type_id]5�_�                       &    ����                                                                                                                                                                                                                                                                                                                            
   $       
   0       v   0    _V     �   
      �      4#search_cols_list = [name, description, tag_type_id]5�_�                       #    ����                                                                                                                                                                                                                                                                                                                            
   $       
   0       v   0    _V     �         �      1#pdf_cols_list = [name, description, tag_type_id]5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                       �          V       _V     �                  �               �             �   #class_name = Tag   #table_name =tag   #prefix =PRE   #postfix =POST   ^#columns_to_create = [id, name, description, tag_type_id] #id - primary_key autoincrement=True   #cont_name =media   #html_template_name =generic   #dbsession =DBSession   !#controller_name =MediaController   2#view_cols_list = [name, description, tag_type_id]   4#search_cols_list = [name, description, tag_type_id]   1#pdf_cols_list = [name, description, tag_type_id]   #link_to_id_or_None =   #link_class_name_None =       ############################   # Controller   ############################           &class MediaController(BaseController):       """Docstring for media."""       (    def __init__(self, *args, **kwargs):           pass       (    @require(predicates.not_anonymous())   +    @expose('rocket_app.templates.generic')   $    def tags(self, *args, **kwargs):   8        html = self.get_active_tag_html(*args, **kwargs)   5        javascript = self.get_javascript_tag_onload()           title = "Tag"   B        return dict(title=title, html=html, javascript=javascript)           @expose()   3    def get_active_tag_html(self, *args, **kwargs):   '        dbase_query = Tag.get_all('id')           outputlist = []            for item in dbase_query:               outputlist.append({   h                'name' : "<div class='edit tag_edit' tag_id='{1}'>{0}</div>".format(item.name, item.id),   1                'description' : item.description,   1                'tag_type_id' : item.tag_type_id,                                })           dbcolumnlist=[                   'name',                   'description',                   'tag_type_id',                       ]           theadlist=[                   'Name',                   'Description',                   'Tag_Type_Id',                   ]   T        htmltbl = build_html_table(outputlist, dbcolumnlist, theadlist, "tag_table")           html = f"""           <div class="row">   #            <div class="col-md-12">   "                <div class="card">   )                <div class="card-header">   ,                    <div class="row d-flex">   .                        <div class="col-md-6">   ;                            <h4 class="card-title">Tag</h4>                           </div>   9                        <div class="col-md-6 text-right">   o                            <button id="create_new_tag" class="btn btn-primary ml-auto">Create New Tag</button>                           </div>                       </div>   ?                    <div class="row d-flex align-items-center">   .                        <div class="col-md-4">   t                            <input type="text" class="form-control search" name="searchphrase" placeholder="Search">                           </div>   .                        <div class="col-md-8">   Y                            <button class="btn btn-primary action_search">Search</button>   J                            <button class="btn btn-primary">Reset</button>                           </div>                       </div>                       <hr>                   </div>   '                <div class="card-body">   2                    <div class="table-responsive">   !                        {htmltbl}                       </div>                   </div>                   </div>               </div>           </div>           """           return html           @expose()   9    def get_javascript_tag_onload(self, *args, **kwargs):           javascript = """   .        $("#create_new_tag").click(function(){   I            $('#dialogdiv').load('/media/get_modal_tag?', function(data){                   return false;               });           });   (        $(".tag_edit").click(function(){   :            var kwargs = 'tag_id='+$(this).attr('tag_id');   Q            $('#dialogdiv').load('/media/get_modal_tag?', kwargs, function(data){                   return false;               });           });           """           return javascript           @expose()   -    def get_modal_tag(self, *args, **kwargs):   +        tag_id = kwargs.get('tag_id', None)           tag = None           hidden_input = ''           if tag_id:   #            tag = Tag.by_id(tag_id)   P            hidden_input = get_hidden_input(**{'id': 'tag_id', 'value': tag_id})   &        name = tag.name if tag else ''   4        description = tag.description if tag else ''   4        tag_type_id = tag.tag_type_id if tag else ''           html = f"""   |        <div class="modal fade" id="dialog_tag" tabindex="-1" role="dialog" aria-labelledby="mytagLabel" aria-hidden="true">   E            <div class="modal-dialog modal-dialog-centered modal-lg">   +                <div class="modal-content">   .                    <div class="modal-header">   .                        <div class="col-md-6">   ?                            <h4 class="card-title">New Tag</h4>                           </div>                       </div>   ,                    <div class="modal-body">   ,                        <form id='form_tag'>   &                        {hidden_input}   6                                <div class="col-md-6">   !					<div class="form-group row">   M						<label class="col-md-3 col-form-label" required for="name">Name</label>   						<div class="col-md-9">   d							<input id="name" value="{name}" type="text" name="name" class="form-control" required='true'>   						</div>   					</div>   
				</div>   6                                <div class="col-md-6">   !					<div class="form-group row">   [						<label class="col-md-3 col-form-label" required for="description">Description</label>   						<div class="col-md-9">   y							<input id="description" value="{description}" type="text" name="description" class="form-control" required='true'>   						</div>   					</div>   
				</div>   6                                <div class="col-md-6">   !					<div class="form-group row">   [						<label class="col-md-3 col-form-label" required for="tag_type_id">Tag_Type_Id</label>   						<div class="col-md-9">   y							<input id="tag_type_id" value="{tag_type_id}" type="text" name="tag_type_id" class="form-control" required='true'>   						</div>   					</div>   
				</div>                           </form>                       </div>   .                    <div class="modal-footer">   S                        <button id='save_tag' class="btn btn-primary">Save</button>   X                        <button class="btn btn-outline-primary tag_back">Cancel</button>                       </div>                   </div>               </div>           </div>           """           javascript = """           <script>   !        var form_id = '#form_tag'   #        setFormValidation(form_id);   (        $('#save_tag').click(function(){   .             var valid = FormIsValid(form_id);                if(valid){   8                var formserial = $(form_id).serialize();   F                $.post('/media/save_tag?', formserial, function(data){   .                    $.redirect('/media/tags');   !                    return false;                   });                }           });   (        $('.tag_back').click(function(){   +            $('#dialog_tag').modal('hide');           });   !        $('#dialog_tag').modal();           </script>   	     	"""            return html + javascript           @expose()   (    def save_tag(self, *args, **kwargs):   4        usernow = request.identity.get('user', None)   +        tag_id = kwargs.get('tag_id', None)           if not tag_id:               this = Tag()   0            this.name = kwargs.get('name', None)   >            this.description = kwargs.get('description', None)   >            this.tag_type_id = kwargs.get('tag_type_id', None)   &            this.added_by = usernow.id               DBSession.add(this)               DBSession.flush()           else:   $            this = Tag.by_id(tag_id)   '            if not this: return 'false'   0            this.name = kwargs.get('name', None)   >            this.description = kwargs.get('description', None)   >            this.tag_type_id = kwargs.get('tag_type_id', None)               DBSession.flush()           return str(this.id)5�_�      
           	      !    ����                                                                                                                                                                                                                                                                                                                                                 V       _V     �   �   �   �                  this = .by_id(_id)�   �   �   �                  this = ()�   ~   �   �                   = .by_id(_id)�   :   <   �      $        dbase_query = .get_all('id')�   +   -   �          Docstring for .�   �   �   �                  $8.flush()�   �   �   �      *            if not this: return 'false'`!p   	snip >> 3   args = get_args(t[5])   )write_saveedit_record(args, snip, t[4]) `�   �   �   �      "            this = $1.by_id($2_id)�   �   �   �                  $8.flush()�   �   �   �                  $8.add(this)�   �   �   �                  this = ()`!p   	snip >> 3   args = get_args(t[5])   (write_savenew_record(args, snip, t[4]) `�   �   �   �                  this = $1()`!p�   �   �   �              if not $2_id:�   �   �   �      )        $2_id = kwargs.get('$2_id', None)�   �   �   �      '    def save_$2(self, *args, **kwargs):�   �   �   �               $('#dialog_$2').modal();�   �   �   �      *            $('#dialog_$2').modal('hide');�   �   �   �      '        $('.$2_back').click(function(){�   �   �   �      *                    $.redirect('/$6/$2s');�   �   �   �      B                $.post('/$6/save_$2?', formserial, function(data){�   �   �   �      '        $('#save_$2').click(function(){�   �   �   �      '        setFormValidation(form_id); `!p   	snip >> 2   snip.rv = ""   args = get_args(t[5])   &write_datepicker_js(args, snip, t[2])`�   �   �   �               var form_id = '#form_$2'�   �   �   �      W                        <button class="btn btn-outline-primary $2_back">Cancel</button>�   �   �   �      R                        <button id='save_$2' class="btn btn-primary">Save</button>�   �   �   �      )                        {hidden_input}`!p   	snip >> 8   args = get_args(t[10])   3write_new_form_cards_with_value(args, snip, t[2]) `�   �   �   �      +                        <form id='form_$2'>�   �   �   �      N                            <h4 class="card-title">New ${2/\w+\s*/\u$0/g}</h4>�   �   �   �      z        <div class="modal fade" id="dialog_$2" tabindex="-1" role="dialog" aria-labelledby="my$2Label" aria-hidden="true">�      �   �      N            hidden_input = get_hidden_input(**{'id': '_id', 'value': _id}) `!p   	snip >> 2   args = get_args(t[10])   (write_edit_form_args(args, snip, t[2]) `�      �   �      R            hidden_input = get_hidden_input(**{'id': '$2_id', 'value': $2_id}) `!p�   ~   �   �                   $2 = $1.by_id($2_id)�   }      �              if $2_id:�   {   }   �              $2 = None�   z   |   �      )        $2_id = kwargs.get('$2_id', None)�   y   {   �      ,    def get_modal_$2(self, *args, **kwargs):�   q   s   �      M            $('#dialogdiv').load('/$6/get_modal_$2?', kwargs, function(data){�   p   r   �      8            var kwargs = '$2_id='+$(this).attr('$2_id');�   o   q   �      '        $(".$2_edit").click(function(){�   k   m   �      E            $('#dialogdiv').load('/$6/get_modal_$2?', function(data){�   j   l   �      -        $("#create_new_$2").click(function(){�   h   j   �      8    def get_javascript_$2_onload(self, *args, **kwargs):�   N   P   �      }                            <button id="create_new_$2" class="btn btn-primary ml-auto">Create New ${2/\w+\s*/\u$0/g}</button>�   K   M   �      J                            <h4 class="card-title">${2/\w+\s*/\u$0/g}</h4>�   C   E   �      S        htmltbl = build_html_table(outputlist, dbcolumnlist, theadlist, "$2_table")�   A   C   �              theadlist=[ `!p   	snip >> 4   snip.rv = ""   args = get_args(t[10])   !write_headers(args, snip, t[4]) `�   ?   A   �              dbcolumnlist=[ `!p   	snip >> 4   snip.rv = ""   args = get_args(t[10])   #write_dictstuff(args, snip, t[4]) `�   =   ?   �      #            outputlist.append({ `!p   	snip >> 4   args = get_args(t[10])   $write_outputlist(args, snip, t[2]) `�   :   <   �      &        dbase_query = $1.get_all('id')�   9   ;   �      2    def get_active_$2_html(self, *args, **kwargs):�   5   7   �      $        title = "${2/\w+\s*/\u$0/g}"�   4   6   �      4        javascript = self.get_javascript_$2_onload()�   3   5   �      7        html = self.get_active_$2_html(*args, **kwargs)�   2   4   �      #    def $2s(self, *args, **kwargs):�   +   -   �      Y    `!p snip.rv = triple_quotes(snip)`Docstring for $6.`!p snip.rv = triple_quotes(snip)`�   *   ,   �      class $9(BaseController):�   )   +   �      $0�   #   %   �      #link_class_name_None =${14}�   "   $   �      #link_to_id_or_None =${13}�   !   #   �      #pdf_cols_list = [$12]�       "   �      #search_cols_list = [$11]�      !   �      #view_cols_list = [$10]�          �      #controller_name =${9}�         �      #dbsession =${8}�         �      #html_template_name =${7}�         �      #cont_name =${6}�         �      >#columns_to_create = [$5] #id - primary_key autoincrement=True�         �      #postfix =${4}�         �      #prefix =${3}�         �      #table_name =${2}�         �      ##class_name = ${1:GenericClassName}�                 !_tgcreateclass_nowui_modal_nojson5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                v       _V     �         �    �   �   �   �      .            this = GenericClassName.by_id(_id)�   �   �   �      %            this = GenericClassName()�   ~   �   �      *             = GenericClassName.by_id(_id)�   :   <   �      4        dbase_query = GenericClassName.get_all('id')�         �      #class_name = GenericClassName5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                v       _V     �   �   �   �                  this = .by_id(_id)�   �   �   �                  this = ()�   ~   �   �                   = .by_id(_id)�   :   <   �      $        dbase_query = .get_all('id')�         �      #class_name = �         �    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       _V     �   �   �   �      !            this = Tag.by_id(_id)�   �   �   �              if not _id:�   �   �   �      %        _id = kwargs.get('_id', None)�   �   �   �      %    def save_(self, *args, **kwargs):�   �   �   �              $('#dialog_').modal();�   �   �   �      (            $('#dialog_').modal('hide');�   �   �   �      %        $('._back').click(function(){�   �   �   �      &                    $.redirect('//s');�   �   �   �      >                $.post('//save_?', formserial, function(data){�   �   �   �      %        $('#save_').click(function(){�   �   �   �              var form_id = '#form_'�   �   �   �      U                        <button class="btn btn-outline-primary _back">Cancel</button>�   �   �   �      P                        <button id='save_' class="btn btn-primary">Save</button>�   �   �   �      )                        <form id='form_'>�   �   �   �      <                            <h4 class="card-title">New </h4>�   �   �   �      v        <div class="modal fade" id="dialog_" tabindex="-1" role="dialog" aria-labelledby="myLabel" aria-hidden="true">�      �   �      K            hidden_input = get_hidden_input(**{'id': '_id', 'value': _id}) �   ~   �   �                   = Tag.by_id(_id)�   }      �              if _id:�   {   }   �               = None�   z   |   �      %        _id = kwargs.get('_id', None)�   y   {   �      *    def get_modal_(self, *args, **kwargs):�   q   s   �      I            $('#dialogdiv').load('//get_modal_?', kwargs, function(data){�   p   r   �      4            var kwargs = '_id='+$(this).attr('_id');�   o   q   �      %        $("._edit").click(function(){�   k   m   �      A            $('#dialogdiv').load('//get_modal_?', function(data){�   j   l   �      +        $("#create_new_").click(function(){�   h   j   �      6    def get_javascript__onload(self, *args, **kwargs):�   N   P   �      i                            <button id="create_new_" class="btn btn-primary ml-auto">Create New </button>�   K   M   �      8                            <h4 class="card-title"></h4>�   C   E   �      Q        htmltbl = build_html_table(outputlist, dbcolumnlist, theadlist, "_table")�   9   ;   �      0    def get_active__html(self, *args, **kwargs):�   5   7   �              title = ""�   4   6   �      2        javascript = self.get_javascript__onload()�   3   5   �      5        html = self.get_active__html(*args, **kwargs)�   2   4   �      !    def s(self, *args, **kwargs):�         �      #table_name =�         �    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       _V     �         �      	#prefix =�         �    5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                v       _V     �         �      
#postfix =�         �    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       _V     �   �   �   �      '            if not this: return 'false'�   �   �   �                  this = Tag()�         �      <#columns_to_create = [] #id - primary_key autoincrement=True�         �    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       _V     �   �   �   �      )                    $.redirect('//tags');�   �   �   �      A                $.post('//save_tag?', formserial, function(data){�   q   s   �      L            $('#dialogdiv').load('//get_modal_tag?', kwargs, function(data){�   k   m   �      D            $('#dialogdiv').load('//get_modal_tag?', function(data){�   +   -   �          """Docstring for ."""�         �      #cont_name =�         �    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       _V     �         �      #html_template_name =�         �    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       _V     �   �   �   �                  .flush()�   �   �   �                  .flush()�   �   �   �                  .add(this)�         �      #dbsession =�         �    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       _V     �   *   ,   �      class (BaseController):�          �      #controller_name =�          �    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       _V     �   �   �   �      &                        {hidden_input}�   �   �   �      Q            hidden_input = get_hidden_input(**{'id': 'tag_id', 'value': tag_id}) �   E   I   �              theadlist=[ �   A   E   �              dbcolumnlist=[ �   =   A   �                   outputlist.append({ �      !   �      #view_cols_list = []�       !   �    5�_�                    !       ����                                                                                                                                                                                                                                                                                                                                                v       _V     �       "   �      #search_cols_list = []�   !   "   �    5�_�                    "       ����                                                                                                                                                                                                                                                                                                                                                v       _V     �   !   #   �      #pdf_cols_list = []�   "   #   �    5�_�                     >        ����                                                                                                                                                                                                                                                                                                                                                v       _V    �   �   �          $        setFormValidation(form_id); �   �   �          5        description = tag.description if tag else '' �   �   �          '        name = tag.name if tag else '' �   �   �          Q            hidden_input = get_hidden_input(**{'id': 'tag_id', 'value': tag_id}) �   G   I                           ' Description', �   F   H                          'Name', �   E   G                  theadlist=[ �   C   E                          'description', �   B   D                          'name', �   A   C                  dbcolumnlist=[ �   ?   A          2                'description' : item.description, �   >   @          j                'name' : "<div class='edit tag_edit' tag_id='{1}'>{0}</div>".format(item.name, item.id),  �   =   ?                       outputlist.append({ 5�_�                    
   $    ����                                                                                                                                                                                                                                                                                                                                         7       v   7    _V     �   	      �      X#view_cols_list = [name, description#search_cols_list = [name, description, tag_type_id]5��