from .models import Page, Follow
from .serializers import PageSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .CustomPermissions import IsStaff ,IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class PageModelViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    ## Set current User to Company Page Owner.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    ## Custom Permissions to Update Page
    def get_permissions(self):
        # Only Authenticated User can create
        
        if(self.action == 'list' or self.action == 'create' or self.action == 'retrieve'):
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsOwnerOrReadOnly]
        
        return super(self.__class__, self).get_permissions()

        
    