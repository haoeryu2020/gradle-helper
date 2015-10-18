import glob
import file_ops as fo
import os
import md5base36 as gradlemd5
import shutil
import sys

gradle_url='http://services.gradle.org/distributions/gradle-2.4-all.zip'
src_dir='~/.gradle/'
gradle_dist_dir='~/.gradle/wrapper/dists/%s/%s/%s'

def copy_one(src, dst):
    shutil.copyfile(src,dst)

def copy_url(url, f):
    print url
    md5b36 = gradlemd5.get_md5b36(url)
    stem, ext = os.path.splitext(f)
    dst = fo.get_path(gradle_dist_dir % (stem, md5b36, f))
    src = fo.get_path("%s/%s" % (src_dir, f))
    parent = os.path.dirname(dst);
    if not os.path.exists(parent):
        os.makedirs(parent)
    print dst
    shutil.copyfile(src,dst)
    gen_links(parent, url)

def gen_link(src, link_name):
    os.chdir(os.path.dirname(src))
    if not os.path.exists(link_name):
        link_src =os.path.basename(src)
        print "%s -> %s" % (link_name, link_src)
        os.symlink(link_src, link_name)

def gen_links(parent_dir, url):
    links = []
    https = url.replace('http://', 'https://')
    links.append(gradlemd5.get_md5b36(https))
    links.append(gradlemd5.get_md5buu(url, 32))
    links.append(gradlemd5.get_md5buu(https, 32))
    for l in links:
        gen_link(parent_dir, l)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help_str='''
    %s <zip_dir> <glob_*>   copy pattern matched zip files
    %s <zip_dir>            copy gradle*.zip in <zip_dir>
'''
        print help_str % (sys.argv[0], sys.argv[0])
        sys.exit(1)
    pattern = 'gradle*.zip'
    if len(sys.argv) >= 3:
        pattern = sys.argv[2]
        print(pattern)

    if len(sys.argv) >= 2:
        src_dir = sys.argv[1]
        print(src_dir)

    prefix=os.path.dirname(gradle_url)
    os.chdir(fo.get_path(src_dir))
    ttt = []
    for f in glob.glob(pattern):
        url='%s/%s' % (prefix,f)
        copy_url(url, f)
