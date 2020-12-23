Vim�UnDo� �E��\}QƑ�����1鼩��eP3Sͪˡ��   �                                   _�3�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             _�3�     �              l   #!/bin/python   # -*- coding: utf-8 -*-       Efrom tg import require, expose, tmpl_context, lurl, request, redirect   'from tg.predicates import not_anonymous   #from tg.exceptions import HTTPFound       !from tg.i18n import ugettext as _   'from tg.i18n import lazy_ugettext as l_       *from rocket.lib.base import BaseController       6# from rocket.controllers.media import MediaController   4from rocket.controllers.setup import SetupController   6from rocket.controllers.common import CommonController   6from rocket.controllers.entity import EntityController   6from rocket.controllers.policy import PolicyController   8from rocket.controllers.sidebar import SidebarController   8from rocket.controllers.profile import ProfileController   8from rocket.controllers.members import MembersController   8from rocket.controllers.product import ProductController   8from rocket.controllers.reports import ReportsController   :from rocket.controllers.location import LocationController   :from rocket.controllers.branding import BrandingController   >from rocket.controllers.useraccess import UserAccessController   Bfrom rocket.controllers.intermediary import IntermediaryController   ?from rocket.controllers.debit_order import DebitOrderController       %class RootController(BaseController):           # media = MediaController()       setup = SetupController()       common = CommonController()       entity = EntityController()       policy = PolicyController()   !    sidebar = SidebarController()   !    profile = ProfileController()   !    members = MembersController()   !    product = ProductController()   !    reports = ReportsController()   #    location = LocationController()   #    branding = BrandingController()   '    useraccess = UserAccessController()   +    intermediary = IntermediaryController()   (    debit_order = DebitOrderController()       #    def _before(self, *args, **kw):   ,        tmpl_context.project_name = "rocket"           @require(not_anonymous())   '    @expose('rocket.templates.generic')       def index(self):   /        html = self.common.get_dashboard_html()   #        title = l_('Rocket | Home')   :        return dict(title=title, html=html, javascript='')       %    @expose('rocket.templates.login')   A    def login(self, came_from=lurl('/'), failure=None, login=''):   H        login_counter = str(request.environ.get('repoze.who.logins', 0))   $        title = l_('Rocket | Login')   #        self.common.audit_visitor()   _        return dict(title=title, login_counter=login_counter, came_from=came_from, login=login)           @expose()   .    def post_login(self, came_from=lurl('/')):            if not request.identity:   K            login_counter = request.environ.get('repoze.who.logins', 0) + 1   X            redirect('/login', params=dict(came_from=came_from, __logins=login_counter))   !        self.common.audit_login()   ,        return HTTPFound(location=came_from)           @expose()   8    def logout(self, came_from=lurl('/logout_handler')):            if not request.identity:   0            return HTTPFound(location=came_from)   "        self.common.audit_logout()   ,        return HTTPFound(location=came_from)           @expose()   /    def post_logout(self, came_from=lurl('/')):   ,        return HTTPFound(location=came_from)       (    @expose('rocket.templates.prelogin')   /    def forgot_password(self, *args, **kwargs):   =        html = self.common.get_forgot_password_html(**kwargs)   I        javascript = self.common.get_forgot_password_javascript(**kwargs)   .        title = l_('Rocket | Forgot Password')   B        return dict(title=title, html=html, javascript=javascript)           @expose()   %    def reset(self, *args, **kwargs):           try:               guid = args[0]           except Exception as e:               redirect('/login')   =        redirect('/useraccess/reset', params={'guid' : guid})       '    @expose('rocket.templates.generic')       def privacy(self):   -        html = self.common.get_privacy_html()   &        title = l_('Rocket | Privacy')   :        return dict(title=title, html=html, javascript='')       '    @expose('rocket.templates.generic')       def terms(self):   +        html = self.common.get_terms_html()   $        title = l_('Rocket | Terms')   :        return dict(title=title, html=html, javascript='')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _�3�     �                   �               5�_�                     �        ����                                                                                                                                                                                                                                                                                                                                                             _�3�    �   �   �           5��