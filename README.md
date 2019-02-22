centos-release-gluster5 provides the YUM repository file for packages of the
CentOS Storage SIG that are used with GlusterFS 5.

This package needs to get build against the following targets so that the
packages land at the right tag for inclusion in CentOS Extras:

 - core6-extras-common-el6.centos (tag: core6-extras-common-candidate)
 - core7-extras-common-el7.centos (tag: core7-extras-common-candidate)

Building the package can be done like this:


    $ rpmbuild -bs \
               --define "_sourcedir $PWD" --define "_srcrpmdir $PWD" \
               --define "dist .el7.centos" \
               centos-release-gluster5.spec

    $ cbs \
           build core7-extras-common-el7.centos \
           centos-release-gluster5-0.9-1.el7.centos.src.rpm

