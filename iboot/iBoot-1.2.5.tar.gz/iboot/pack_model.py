# -*- coding: utf-8 -*-
import os
import platform
import sys
import shutil
import yaml
from distutils.core import setup
from Cython.Build import cythonize


class SoBuilder(object):

    def __init__(self, app_path):
        self.app_path = app_path
        self.base_path = os.path.abspath('.')
        self.build_path = 'build'
        self.build_tmp_path = 'build/tmp'
        if os.path.exists(self.build_path):
            shutil.rmtree(self.build_path)

        py_ver = ''.join(sys.version[0:3].split('.'))
        self.gcc_suffix = '.cpython-{}m-x86_64-linux-gnu.so'.format(py_ver)

    def copy_other_file(self, src_file_path):
        if src_file_path.endswith('__init__.py'):
            if os.path.exists(self.build_path):
                shutil.rmtree(self.build_path)
            raise Exception(print('程序中存在“__init__.py”文件，编译时会出现异常。请删除所有“__init__.py”文件后再编译！'))

        dst_file_path = '{}/{}/{}'.format(self.base_path, self.build_path, src_file_path[len(self.base_path) + 1:])
        dst_path = dst_file_path[:dst_file_path.rfind('/')]
        if not os.path.isdir(dst_path):
            os.makedirs(dst_path)
        shutil.copyfile(src_file_path, dst_file_path)

    def yeild_py(self, path, copy_others=True):
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isdir(file_path) and not file_name.startswith('.'):
                for f in self.yeild_py(file_path, copy_others):
                    yield f
            elif os.path.isfile(file_path):
                ext = os.path.splitext(file_name)[1]
                if ext not in ('.pyc', '.pyx'):
                    if ext == '.py' and not file_name.startswith('__'):
                        yield os.path.join(path, file_name)
                    elif copy_others:
                        self.copy_other_file(file_path)
            else:
                pass

    def delete_c_files(self, path):
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isdir(file_path) and not file_name.startswith('.'):
                self.delete_c_files(file_path)
            elif os.path.isfile(file_path):
                ext = os.path.splitext(file_name)[1]
                if ext == '.c':
                    os.remove(file_path)
            else:
                pass

    def build_so(self):
        py_files = list(self.yeild_py(os.path.join(self.base_path, self.app_path)))

        try:
            for src_file_path in py_files:
                dst_file_path = '{}/{}/{}'.format(self.base_path, self.build_path,
                                                  src_file_path[len(self.base_path) + 1:])
                idx = dst_file_path.rfind('/')
                dst_path = dst_file_path[:idx]
                py_name = dst_file_path[idx + 1:].split('.')[0]
                setup(ext_modules=cythonize(src_file_path),
                      script_args=['build_ext', '-b', dst_path, '-t', self.build_tmp_path])
                src = dst_path + '/' + py_name + self.gcc_suffix
                dst = dst_path + '/' + py_name + '.so'
                os.rename(src, dst)
        except Exception as e:
            print(str(e))

        self.delete_c_files(os.path.join(self.base_path, self.app_path))
        if os.path.exists(self.build_tmp_path):
            shutil.rmtree(self.build_tmp_path)


def get_model_name():
    try:
        with open('./application.yml', 'rb') as f:
            yml = yaml.load(f, Loader=yaml.SafeLoader)
    except:
        print('错误： 模型配置文件application.yml不存在！')
        return None

    try:
        name = yml['model']['name']
    except:
        print('错误： 未指定模型名称！')
        print('请在application.yml文件中编辑修改...')
        return None

    try:
        python = str(yml['python']['version'])
    except:
        print('错误： 未指定Python版本号！')
        print('请在application.yml文件中编辑修改...')
        return None


    if not python.startswith('3.'):
        print('错误： Python版本号必须是3且3.5以上！')
        print('请在application.yml文件中编辑修改...')
        return None

    if not sys.version.startswith(python):
        print('错误： 声明的Python版本号与当前运行环境（{}）不一致！'.format(sys.version[:sys.version.find(' ')]))
        print('请在application.yml文件中编辑修改...')
        return None

    try:
        model_runner = yml['model_runner']['version']
    except:
        print('错误： 未指定model_runner版本号！')
        print('请在application.yml文件中编辑修改...')
        return None

    if model_runner != 'v2':
        print('错误： model_runner版本号必须是“v2”！')
        print('请在application.yml文件中编辑修改...')
        return None

    if not os.path.exists('requirements.txt'):
        print('错误： requirements.txt文件不存在！')
        return None

    return name


def pack_model():
    name = get_model_name()
    if name is None:
        return

    with open('./application.yml', 'rb') as f:
        yml = yaml.load(f, Loader=yaml.SafeLoader)

    try:
        build_web = yml['build']['build_web']
    except:
        build_web = True

    try:
        build_so = yml['build']['compile_python_to_so']
    except:
        build_so = False

    is_windows = platform.system() == 'Windows'

    if is_windows:
        os.system('rd /s /q out')
        os.system('mkdir out')
        os.system('mkdir out\\{}'.format(name))
        os.system('copy application.yml out\\{}\\'.format(name))
        os.system('copy requirements.txt out\\{}\\'.format(name))
    else:
        os.system('rm -rf ./out')
        os.system('mkdir out')
        os.system('mkdir out/{}'.format(name))
        os.system('cp ./application.yml ./out/{}/'.format(name))
        os.system('cp ./requirements.txt ./out/{}/'.format(name))

    if build_so:
        so_builder = SoBuilder('core')
        so_builder.build_so()
        if is_windows:
            os.system('move /y /q build\\core out\\{}\\'.format(name))
        else:
            os.system('mv ./build/core ./out/{}/'.format(name))
        shutil.rmtree('build')
    else:
        if is_windows:
            os.system('mkdir out\\{}\\core'.format(name))
            os.system('xcopy /y /q /s /e core\\ out\\{}\\core\\'.format(name))
        else:
            os.system('cp -rf ./core ./out/{}/'.format(name))

    if build_web:
        if os.path.exists('./webapp/src'):
            cwd = os.getcwd()
            os.chdir(os.path.join(cwd, 'webapp'))
            if not os.path.exists('./node_modules'):
                os.system('npm install')
            os.system('ng build --prod')
            os.chdir(cwd)
        if os.path.exists('./webapp/www'):
            if is_windows:
                os.system('mkdir out\\{}\\webapp\\www'.format(name))
                os.system('xcopy /y /q /s /e webapp\\www\\ out\\{}\\webapp\\www\\'.format(name))
            else:
                os.system('mkdir out/{}/webapp'.format(name))
                os.system('cp -rf ./webapp/www ./out/{}/webapp/'.format(name))

    dst_path = './out/{}'.format(name)
    shutil.make_archive(dst_path, 'zip', dst_path)  # 将目标文件夹自动压缩成.zip文件
    shutil.rmtree('./out/{}/'.format(name))
    print('模型打包完成！ 输出位置： ./out/{}.zip'.format(name))


def build_docker():
    name = get_model_name()
    if name is None:
        return

    with open('./application.yml', 'rb') as f:
        yml = yaml.load(f, Loader=yaml.SafeLoader)

    try:
        image_name = yml['build']['image_name']
    except:
        print('错误： 未指定docker镜像名称！')
        print('请在application.yml文件中编辑修改...')
        return

    try:
        image_tag = str(yml['build']['tag'])
    except:
        print('未指定docker镜像tag，使用：latest')
        image_tag = 'latest'

    try:
        build_web = yml['build']['build_web']
    except:
        build_web = True

    try:
        build_so = yml['build']['compile_python_to_so']
    except:
        build_so = False

    is_windows = platform.system() == 'Windows'

    if is_windows:
        os.system('rd /s /q temp')
        os.system('mkdir temp')
        os.system('xcopy /q application.yml temp')
        os.system('xcopy /q requirements.txt temp')
        os.system('xcopy /q Dockerfile temp')
    else:
        os.system('rm -rf temp')
        os.system('mkdir temp')
        os.system('cp ./application.yml ./temp')
        os.system('cp ./requirements.txt ./temp')
        os.system('cp ./Dockerfile ./temp')

    if build_so:
        so_builder = SoBuilder('core')
        so_builder.build_so()
        if is_windows:
            os.system('move /y /q build\\core temp')
        else:
            os.system('mv ./build/core ./temp/')
        shutil.rmtree('build')
    else:
        if is_windows:
            os.system('mkdir temp\\core')
            os.system('xcopy /y /q /s /e core temp\\core')
        else:
            os.system('cp -rf ./core ./temp/')

    if build_web:
        if os.path.exists('./webapp/src'):
            cwd = os.getcwd()
            os.chdir(os.path.join(cwd, 'webapp'))
            if not os.path.exists('./node_modules'):
                os.system('npm install')
            os.system('ng build --prod')
            os.chdir(cwd)
        if os.path.exists('./webapp/www'):
            if is_windows:
                os.system('mkdir temp\\webapp\\www')
                os.system('xcopy /y /q /s /e webapp\\www\\ temp\\webapp\\www\\')
            else:
                os.system('mkdir temp/webapp')
                os.system('cp -rf ./webapp/www ./temp/webapp/')

    os.system('docker image rm {}:{}'.format(image_name, image_tag))
    os.system('docker build -t {}:{} ./temp'.format(image_name, image_tag))
    if is_windows:
        os.system('rd /s /q temp')
    else:
        os.system('rm -rf temp')

    print('模型docker镜像 {}:{} 构建完成！ '.format(image_name, image_tag))


if __name__ == '__main__':
    pack_model()
