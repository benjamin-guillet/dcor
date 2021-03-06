# URLconfig and simple views functions generated by docGen script.
# Created Thu Jul 21 10:43:19 2011

from django.conf.urls.defaults import *
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import HttpResponse

# A list of items to display in the index, as tuples of (displayName, href).
index_list = [
	('hipercore', 'hipercore.html'), 
	('hipercore.authenticore', 'hipercore.authenticore.html'), 
	('hipercore.authenticore.decorators', 'hipercore.authenticore.decorators.html'), 
	('hipercore.authenticore.backends', 'hipercore.authenticore.backends.html'), 
	('hipercore.authenticore.middleware', 'hipercore.authenticore.middleware.html'), 
	('hipercore.authenticore.tests', 'hipercore.authenticore.tests.html'), 
	('hipercore.authenticore.tests.decorators', 'hipercore.authenticore.tests.decorators.html'), 
	('hipercore.authenticore.tests.tokens', 'hipercore.authenticore.tests.tokens.html'), 
	('hipercore.authenticore.tests.basic', 'hipercore.authenticore.tests.basic.html'), 
	('hipercore.authenticore.tests.urls', 'hipercore.authenticore.tests.urls.html'), 
	('hipercore.authenticore.tests.auth_backends', 'hipercore.authenticore.tests.auth_backends.html'), 
	('hipercore.authenticore.tests.views', 'hipercore.authenticore.tests.views.html'), 
	('hipercore.authenticore.tests.models', 'hipercore.authenticore.tests.models.html'), 
	('hipercore.authenticore.tests.forms', 'hipercore.authenticore.tests.forms.html'), 
	('hipercore.authenticore.tests.remote_user', 'hipercore.authenticore.tests.remote_user.html'), 
	('hipercore.authenticore.tokens', 'hipercore.authenticore.tokens.html'), 
	('hipercore.authenticore.create_superuser', 'hipercore.authenticore.create_superuser.html'), 
	('hipercore.authenticore.management', 'hipercore.authenticore.management.html'), 
	('hipercore.authenticore.management.commands', 'hipercore.authenticore.management.commands.html'), 
	('hipercore.authenticore.management.commands.changepassword', 'hipercore.authenticore.management.commands.changepassword.html'), 
	('hipercore.authenticore.management.commands.createsuperuser', 'hipercore.authenticore.management.commands.createsuperuser.html'), 
	('hipercore.authenticore.urls', 'hipercore.authenticore.urls.html'), 
	('hipercore.authenticore.context_processors', 'hipercore.authenticore.context_processors.html'), 
	('hipercore.authenticore.models', 'hipercore.authenticore.models.html'), 
	('hipercore.authenticore.admin', 'hipercore.authenticore.admin.html'), 
	('hipercore.authenticore.forms', 'hipercore.authenticore.forms.html'), 
	('hipercore.authenticore.handlers', 'hipercore.authenticore.handlers.html'), 
	('hipercore.permissions', 'hipercore.permissions.html'), 
	('hipercore.documentation', 'hipercore.documentation.html'), 
	('hipercore.documentation.urls', 'hipercore.documentation.urls.html'), 
	('hipercore.documentation.views', 'hipercore.documentation.views.html'), 
	('hipercore.epyUrls', 'hipercore.epyUrls.html'), 
	('hipercore.admin', 'hipercore.admin.html'), 
	('hipercore.admin.templatetags', 'hipercore.admin.templatetags.html'), 
	('hipercore.admin.templatetags.adminmedia', 'hipercore.admin.templatetags.adminmedia.html'), 
	('hipercore.admin.templatetags.admin_list', 'hipercore.admin.templatetags.admin_list.html'), 
	('hipercore.admin.templatetags.log', 'hipercore.admin.templatetags.log.html'), 
	('hipercore.admin.templatetags.admin_modify', 'hipercore.admin.templatetags.admin_modify.html'), 
	('hipercore.admin.widgets', 'hipercore.admin.widgets.html'), 
	('hipercore.admin.hipercicViewHelpers', 'hipercore.admin.hipercicViewHelpers.html'), 
	('hipercore.admin.helpers', 'hipercore.admin.helpers.html'), 
	('hipercore.admin.views', 'hipercore.admin.views.html'), 
	('hipercore.admin.views.decorators', 'hipercore.admin.views.decorators.html'), 
	('hipercore.admin.views.main', 'hipercore.admin.views.main.html'), 
	('hipercore.admin.views.hipercic_home', 'hipercore.admin.views.hipercic_home.html'), 
	('hipercore.admin.sites', 'hipercore.admin.sites.html'), 
	('hipercore.admin.actions', 'hipercore.admin.actions.html'), 
	('hipercore.admin.options', 'hipercore.admin.options.html'), 
	('hipercore.admin.validation', 'hipercore.admin.validation.html'), 
	('hipercore.admin.models', 'hipercore.admin.models.html'), 
	('hipercore.admin.util', 'hipercore.admin.util.html'), 
	('hipercore.admin.adminConfig', 'hipercore.admin.adminConfig.html'), 
	('hipercore.admin.filterspecs', 'hipercore.admin.filterspecs.html'), 
	('hipercore.docGen', 'hipercore.docGen.html'), 
	('hipercore.docGen.main', 'hipercore.docGen.main.html'), 
	('hipercore.docGen.src', 'hipercore.docGen.src.html'), 
	('hipercore.docGen.src.core', 'hipercore.docGen.src.core.html'), 
	('hipercore.docGen.src.importer', 'hipercore.docGen.src.importer.html'), 
	('hipercore.docGen.src.out', 'hipercore.docGen.src.out.html'), 
	('hipercore.docGen.src.doc', 'hipercore.docGen.src.doc.html'), 
	]
def hipercore_html(request):
	return render_to_response("api/hipercore.html", {})

def hipercore_authenticore_html(request):
	return render_to_response("api/hipercore.authenticore.html", {})

def hipercore_authenticore_decorators_html(request):
	return render_to_response("api/hipercore.authenticore.decorators.html", {})

def hipercore_authenticore_backends_html(request):
	return render_to_response("api/hipercore.authenticore.backends.html", {})

def hipercore_authenticore_middleware_html(request):
	return render_to_response("api/hipercore.authenticore.middleware.html", {})

def hipercore_authenticore_tests_html(request):
	return render_to_response("api/hipercore.authenticore.tests.html", {})

def hipercore_authenticore_tests_decorators_html(request):
	return render_to_response("api/hipercore.authenticore.tests.decorators.html", {})

def hipercore_authenticore_tests_tokens_html(request):
	return render_to_response("api/hipercore.authenticore.tests.tokens.html", {})

def hipercore_authenticore_tests_basic_html(request):
	return render_to_response("api/hipercore.authenticore.tests.basic.html", {})

def hipercore_authenticore_tests_urls_html(request):
	return render_to_response("api/hipercore.authenticore.tests.urls.html", {})

def hipercore_authenticore_tests_auth_backends_html(request):
	return render_to_response("api/hipercore.authenticore.tests.auth_backends.html", {})

def hipercore_authenticore_tests_views_html(request):
	return render_to_response("api/hipercore.authenticore.tests.views.html", {})

def hipercore_authenticore_tests_models_html(request):
	return render_to_response("api/hipercore.authenticore.tests.models.html", {})

def hipercore_authenticore_tests_forms_html(request):
	return render_to_response("api/hipercore.authenticore.tests.forms.html", {})

def hipercore_authenticore_tests_remote_user_html(request):
	return render_to_response("api/hipercore.authenticore.tests.remote_user.html", {})

def hipercore_authenticore_tokens_html(request):
	return render_to_response("api/hipercore.authenticore.tokens.html", {})

def hipercore_authenticore_create_superuser_html(request):
	return render_to_response("api/hipercore.authenticore.create_superuser.html", {})

def hipercore_authenticore_management_html(request):
	return render_to_response("api/hipercore.authenticore.management.html", {})

def hipercore_authenticore_management_commands_html(request):
	return render_to_response("api/hipercore.authenticore.management.commands.html", {})

def hipercore_authenticore_management_commands_changepassword_html(request):
	return render_to_response("api/hipercore.authenticore.management.commands.changepassword.html", {})

def hipercore_authenticore_management_commands_createsuperuser_html(request):
	return render_to_response("api/hipercore.authenticore.management.commands.createsuperuser.html", {})

def hipercore_authenticore_urls_html(request):
	return render_to_response("api/hipercore.authenticore.urls.html", {})

def hipercore_authenticore_context_processors_html(request):
	return render_to_response("api/hipercore.authenticore.context_processors.html", {})

def hipercore_authenticore_models_html(request):
	return render_to_response("api/hipercore.authenticore.models.html", {})

def hipercore_authenticore_admin_html(request):
	return render_to_response("api/hipercore.authenticore.admin.html", {})

def hipercore_authenticore_forms_html(request):
	return render_to_response("api/hipercore.authenticore.forms.html", {})

def hipercore_authenticore_handlers_html(request):
	return render_to_response("api/hipercore.authenticore.handlers.html", {})

def hipercore_permissions_html(request):
	return render_to_response("api/hipercore.permissions.html", {})

def hipercore_documentation_html(request):
	return render_to_response("api/hipercore.documentation.html", {})

def hipercore_documentation_urls_html(request):
	return render_to_response("api/hipercore.documentation.urls.html", {})

def hipercore_documentation_views_html(request):
	return render_to_response("api/hipercore.documentation.views.html", {})

def hipercore_epyUrls_html(request):
	return render_to_response("api/hipercore.epyUrls.html", {})

def hipercore_admin_html(request):
	return render_to_response("api/hipercore.admin.html", {})

def hipercore_admin_templatetags_html(request):
	return render_to_response("api/hipercore.admin.templatetags.html", {})

def hipercore_admin_templatetags_adminmedia_html(request):
	return render_to_response("api/hipercore.admin.templatetags.adminmedia.html", {})

def hipercore_admin_templatetags_admin_list_html(request):
	return render_to_response("api/hipercore.admin.templatetags.admin_list.html", {})

def hipercore_admin_templatetags_log_html(request):
	return render_to_response("api/hipercore.admin.templatetags.log.html", {})

def hipercore_admin_templatetags_admin_modify_html(request):
	return render_to_response("api/hipercore.admin.templatetags.admin_modify.html", {})

def hipercore_admin_widgets_html(request):
	return render_to_response("api/hipercore.admin.widgets.html", {})

def hipercore_admin_hipercicViewHelpers_html(request):
	return render_to_response("api/hipercore.admin.hipercicViewHelpers.html", {})

def hipercore_admin_helpers_html(request):
	return render_to_response("api/hipercore.admin.helpers.html", {})

def hipercore_admin_views_html(request):
	return render_to_response("api/hipercore.admin.views.html", {})

def hipercore_admin_views_decorators_html(request):
	return render_to_response("api/hipercore.admin.views.decorators.html", {})

def hipercore_admin_views_main_html(request):
	return render_to_response("api/hipercore.admin.views.main.html", {})

def hipercore_admin_views_hipercic_home_html(request):
	return render_to_response("api/hipercore.admin.views.hipercic_home.html", {})

def hipercore_admin_sites_html(request):
	return render_to_response("api/hipercore.admin.sites.html", {})

def hipercore_admin_actions_html(request):
	return render_to_response("api/hipercore.admin.actions.html", {})

def hipercore_admin_options_html(request):
	return render_to_response("api/hipercore.admin.options.html", {})

def hipercore_admin_validation_html(request):
	return render_to_response("api/hipercore.admin.validation.html", {})

def hipercore_admin_models_html(request):
	return render_to_response("api/hipercore.admin.models.html", {})

def hipercore_admin_util_html(request):
	return render_to_response("api/hipercore.admin.util.html", {})

def hipercore_admin_adminConfig_html(request):
	return render_to_response("api/hipercore.admin.adminConfig.html", {})

def hipercore_admin_filterspecs_html(request):
	return render_to_response("api/hipercore.admin.filterspecs.html", {})

def hipercore_docGen_html(request):
	return render_to_response("api/hipercore.docGen.html", {})

def hipercore_docGen_main_html(request):
	return render_to_response("api/hipercore.docGen.main.html", {})

def hipercore_docGen_src_html(request):
	return render_to_response("api/hipercore.docGen.src.html", {})

def hipercore_docGen_src_core_html(request):
	return render_to_response("api/hipercore.docGen.src.core.html", {})

def hipercore_docGen_src_importer_html(request):
	return render_to_response("api/hipercore.docGen.src.importer.html", {})

def hipercore_docGen_src_out_html(request):
	return render_to_response("api/hipercore.docGen.src.out.html", {})

def hipercore_docGen_src_doc_html(request):
	return render_to_response("api/hipercore.docGen.src.doc.html", {})

def index(request):
	return render_to_response("api/index.html",{'index_list':index_list, 'title':'Pydoc API', 'updatedDate':"Thu, Jul 21 2011, 10:10AM"})


urlpatterns = patterns('',
	(r'^hipercore.html$', hipercore_html), 
	(r'^hipercore.authenticore.html$', hipercore_authenticore_html), 
	(r'^hipercore.authenticore.decorators.html$', hipercore_authenticore_decorators_html), 
	(r'^hipercore.authenticore.backends.html$', hipercore_authenticore_backends_html), 
	(r'^hipercore.authenticore.middleware.html$', hipercore_authenticore_middleware_html), 
	(r'^hipercore.authenticore.tests.html$', hipercore_authenticore_tests_html), 
	(r'^hipercore.authenticore.tests.decorators.html$', hipercore_authenticore_tests_decorators_html), 
	(r'^hipercore.authenticore.tests.tokens.html$', hipercore_authenticore_tests_tokens_html), 
	(r'^hipercore.authenticore.tests.basic.html$', hipercore_authenticore_tests_basic_html), 
	(r'^hipercore.authenticore.tests.urls.html$', hipercore_authenticore_tests_urls_html), 
	(r'^hipercore.authenticore.tests.auth_backends.html$', hipercore_authenticore_tests_auth_backends_html), 
	(r'^hipercore.authenticore.tests.views.html$', hipercore_authenticore_tests_views_html), 
	(r'^hipercore.authenticore.tests.models.html$', hipercore_authenticore_tests_models_html), 
	(r'^hipercore.authenticore.tests.forms.html$', hipercore_authenticore_tests_forms_html), 
	(r'^hipercore.authenticore.tests.remote_user.html$', hipercore_authenticore_tests_remote_user_html), 
	(r'^hipercore.authenticore.tokens.html$', hipercore_authenticore_tokens_html), 
	(r'^hipercore.authenticore.create_superuser.html$', hipercore_authenticore_create_superuser_html), 
	(r'^hipercore.authenticore.management.html$', hipercore_authenticore_management_html), 
	(r'^hipercore.authenticore.management.commands.html$', hipercore_authenticore_management_commands_html), 
	(r'^hipercore.authenticore.management.commands.changepassword.html$', hipercore_authenticore_management_commands_changepassword_html), 
	(r'^hipercore.authenticore.management.commands.createsuperuser.html$', hipercore_authenticore_management_commands_createsuperuser_html), 
	(r'^hipercore.authenticore.urls.html$', hipercore_authenticore_urls_html), 
	(r'^hipercore.authenticore.context_processors.html$', hipercore_authenticore_context_processors_html), 
	(r'^hipercore.authenticore.models.html$', hipercore_authenticore_models_html), 
	(r'^hipercore.authenticore.admin.html$', hipercore_authenticore_admin_html), 
	(r'^hipercore.authenticore.forms.html$', hipercore_authenticore_forms_html), 
	(r'^hipercore.authenticore.handlers.html$', hipercore_authenticore_handlers_html), 
	(r'^hipercore.permissions.html$', hipercore_permissions_html), 
	(r'^hipercore.documentation.html$', hipercore_documentation_html), 
	(r'^hipercore.documentation.urls.html$', hipercore_documentation_urls_html), 
	(r'^hipercore.documentation.views.html$', hipercore_documentation_views_html), 
	(r'^hipercore.epyUrls.html$', hipercore_epyUrls_html), 
	(r'^hipercore.admin.html$', hipercore_admin_html), 
	(r'^hipercore.admin.templatetags.html$', hipercore_admin_templatetags_html), 
	(r'^hipercore.admin.templatetags.adminmedia.html$', hipercore_admin_templatetags_adminmedia_html), 
	(r'^hipercore.admin.templatetags.admin_list.html$', hipercore_admin_templatetags_admin_list_html), 
	(r'^hipercore.admin.templatetags.log.html$', hipercore_admin_templatetags_log_html), 
	(r'^hipercore.admin.templatetags.admin_modify.html$', hipercore_admin_templatetags_admin_modify_html), 
	(r'^hipercore.admin.widgets.html$', hipercore_admin_widgets_html), 
	(r'^hipercore.admin.hipercicViewHelpers.html$', hipercore_admin_hipercicViewHelpers_html), 
	(r'^hipercore.admin.helpers.html$', hipercore_admin_helpers_html), 
	(r'^hipercore.admin.views.html$', hipercore_admin_views_html), 
	(r'^hipercore.admin.views.decorators.html$', hipercore_admin_views_decorators_html), 
	(r'^hipercore.admin.views.main.html$', hipercore_admin_views_main_html), 
	(r'^hipercore.admin.views.hipercic_home.html$', hipercore_admin_views_hipercic_home_html), 
	(r'^hipercore.admin.sites.html$', hipercore_admin_sites_html), 
	(r'^hipercore.admin.actions.html$', hipercore_admin_actions_html), 
	(r'^hipercore.admin.options.html$', hipercore_admin_options_html), 
	(r'^hipercore.admin.validation.html$', hipercore_admin_validation_html), 
	(r'^hipercore.admin.models.html$', hipercore_admin_models_html), 
	(r'^hipercore.admin.util.html$', hipercore_admin_util_html), 
	(r'^hipercore.admin.adminConfig.html$', hipercore_admin_adminConfig_html), 
	(r'^hipercore.admin.filterspecs.html$', hipercore_admin_filterspecs_html), 
	(r'^hipercore.docGen.html$', hipercore_docGen_html), 
	(r'^hipercore.docGen.main.html$', hipercore_docGen_main_html), 
	(r'^hipercore.docGen.src.html$', hipercore_docGen_src_html), 
	(r'^hipercore.docGen.src.core.html$', hipercore_docGen_src_core_html), 
	(r'^hipercore.docGen.src.importer.html$', hipercore_docGen_src_importer_html), 
	(r'^hipercore.docGen.src.out.html$', hipercore_docGen_src_out_html), 
	(r'^hipercore.docGen.src.doc.html$', hipercore_docGen_src_doc_html), 
	(r'^$',index)
	)
