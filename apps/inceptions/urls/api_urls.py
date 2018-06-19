# coding:utf-8
from django.conf.urls import url
from .. import api
from rest_framework_bulk.routes import BulkRouter

app_name = 'inceptions'


router = BulkRouter()
router.register(r'v1/inceptions', api.InceptionViewSet, 'inception')
router.register(r'v1/dbhosts', api.DbHostViewSet, 'dbhost')
# router.register(r'v1/system-user', api.SystemUserViewSet, 'system-user')
# router.register(r'v1/labels', api.LabelViewSet, 'label')
# router.register(r'v1/nodes', api.NodeViewSet, 'node')
# router.register(r'v1/domain', api.DomainViewSet, 'domain')
# router.register(r'v1/gateway', api.GatewayViewSet, 'gateway')

urlpatterns = [
    url(r'^v1/inceptions-bulk/$', api.InceptionListUpdateApi.as_view(), name='inception-bulk-update'),
    # url(r'^v1/system-user/(?P<pk>[0-9a-zA-Z\-]{36})/auth-info/', api.SystemUserAuthInfoApi.as_view(),name='system-user-auth-info'),
    # url(r'^v1/inceptions/(?P<pk>[0-9a-zA-Z\-]{36})/refresh/$',api.InceptionRefreshHardwareApi.as_view(), name='inception-refresh'),
    # url(r'^v1/inceptions/(?P<pk>[0-9a-zA-Z\-]{36})/alive/$', api.InceptionAdminUserTestApi.as_view(), name='inception-alive-test'),
    # url(r'^v1/admin-user/(?P<pk>[0-9a-zA-Z\-]{36})/nodes/$',        api.ReplaceNodesAdminUserApi.as_view(), name='replace-nodes-admin-user'),
    # url(r'^v1/admin-user/(?P<pk>[0-9a-zA-Z\-]{36})/auth/$',        api.AdminUserAuthApi.as_view(), name='admin-user-auth'),
    # url(r'^v1/admin-user/(?P<pk>[0-9a-zA-Z\-]{36})/connective/$',        api.AdminUserTestConnectiveApi.as_view(), name='admin-user-connective'),
    # url(r'^v1/system-user/(?P<pk>[0-9a-zA-Z\-]{36})/push/$',        api.SystemUserPushApi.as_view(), name='system-user-push'),
    # url(r'^v1/system-user/(?P<pk>[0-9a-zA-Z\-]{36})/connective/$',        api.SystemUserTestConnectiveApi.as_view(), name='system-user-connective'),
    # url(r'^v1/nodes/(?P<pk>[0-9a-zA-Z\-]{36})/children/$',        api.NodeChildrenApi.as_view(), name='node-children'),
    # url(r'^v1/nodes/children/$', api.NodeChildrenApi.as_view(), name='node-children-2'),
    # url(r'^v1/nodes/(?P<pk>[0-9a-zA-Z\-]{36})/children/add/$',        api.NodeAddChildrenApi.as_view(), name='node-add-children'),
    # url(r'^v1/nodes/(?P<pk>[0-9a-zA-Z\-]{36})/inceptions/$',        api.NodeInceptionsApi.as_view(), name='node-inceptions'),
    # url(r'^v1/nodes/(?P<pk>[0-9a-zA-Z\-]{36})/inceptions/add/$',        api.NodeAddInceptionsApi.as_view(), name='node-add-inceptions'),
    # url(r'^v1/nodes/(?P<pk>[0-9a-zA-Z\-]{36})/inceptions/replace/$',        api.NodeReplaceInceptionsApi.as_view(), name='node-replace-inceptions'),
    # url(r'^v1/nodes/(?P<pk>[0-9a-zA-Z\-]{36})/inceptions/remove/$',        api.NodeRemoveInceptionsApi.as_view(), name='node-remove-inceptions'),
    # url(r'^v1/nodes/(?P<pk>[0-9a-zA-Z\-]{36})/refresh-hardware-info/$',        api.RefreshNodeHardwareInfoApi.as_view(), name='node-refresh-hardware-info'),
    # url(r'^v1/nodes/(?P<pk>[0-9a-zA-Z\-]{36})/test-connective/$',        api.TestNodeConnectiveApi.as_view(), name='node-test-connective'),

    # url(r'^v1/gateway/(?P<pk>[0-9a-zA-Z\-]{36})/test-connective/$',        api.GatewayTestConnectionApi.as_view(), name='test-gateway-connective'),
]

urlpatterns += router.urls