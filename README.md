centos-release-gluster-legacy removes unmaintained versions of
centos-release-gluster* packages from the system..

This package needs to get build against the following targets so that the
packages land at the right tag for inclusion in CentOS Extras:

 - core6-extras-common-el6.centos (tag: core6-extras-common-candidate)
 - core7-extras-common-el7.centos (tag: core7-extras-common-candidate)

Building the package can be done like this:


    $ rpmbuild -bs \
               --define "_sourcedir $PWD" --define "_srcrpmdir $PWD" \
               --define "dist .el7.centos" \
               centos-release-gluster-legacy.spec

    $ cbs \
           build core7-extras-common-el7.centos \
           centos-release-gluster-legacy-3.10-1.el7.centos.src.rpm

