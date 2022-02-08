# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_what2eat']

package_data = \
{'': ['*'], 'nonebot_plugin_what2eat': ['resource/*']}

install_requires = \
['nonebot-plugin-apscheduler>=0.1.2,<0.2.0', 'ujson>=5.1.0,<6.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-what2eat',
    'version': '0.1.3',
    'description': 'What to eat today for your breakfast, lunch, dinner and even midnight snack!',
    'long_description': '<div align="center">\n\n# What to Eat\n\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable-next-line MD036 -->\n_🍔🌮🍜🍮🍣🍻🍩 今天吃什么 🍩🍻🍣🍮🍜🌮🍔_\n<!-- prettier-ignore-end -->\n\n</div>\n\n<p align="center">\n  \n  <a href="https://github.com/KafCoppelia/nonebot_plugin_what2eat/blob/main/LICENSE">\n    <img src="https://img.shields.io/badge/license-MIT-informational">\n  </a>\n  \n  <a href="https://github.com/nonebot/nonebot2">\n    <img src="https://img.shields.io/badge/nonebot2-2.0.0alpha.16-green">\n  </a>\n  \n  <a href="">\n    <img src="https://img.shields.io/badge/release-v0.1.3-orange">\n  </a>\n  \n</p>\n\n</p>\n\n## 版本\n\nv0.1.3 与**v0.2.3 for beta.1**版本同步\n\n⚠ 适配nonebot2-2.0.0beta.1；适配beta.1版本参见[beta.1分支](https://github.com/KafCoppelia/nonebot_plugin_what2eat/tree/beta.1)\n\n[更新日志](https://github.com/KafCoppelia/nonebot_plugin_what2eat/releases/tag/v0.1.3)\n\n## 安装\n\n1. 通过`pip`或`nb`，版本请指定`0.1.3`\n\n2. 数据默认位于`./resource/data.json`与`./resource/greating.json`，可通过设置`env`下`WHAT2EAT_PATH`更改；基础菜单、群特色菜单及群友询问Bot次数会记录在该文件中；\n\n## 功能\n\n1. 选择恐惧症？让Bot建议你今天吃什么！\n\n2. 每餐每个时间段询问Bot建议上限可通过`EATING_LIMIT`修改（默认6次），每日6点、11点、17点、22点（夜宵）自动刷新；\n\n3. 群管理可自行添加或移除群特色菜单（`data.json`下`[group_food][group_id]`）；超管可添加或移除基础菜单（`[basic_food]`）；\n\n4. 各群特色菜单相互独立；各群每个时间段询问Bot建议次数独立；Bot会综合各群菜单+基础菜单给出建议；\n\n5. 提醒按时吃饭小助手：每天7、12、15、18、22点群发**问候语**提醒群友按时吃饭/摸鱼，`GROUPS_ID`设置需要群发的群号列表，形如：\n\n    ```python\n    ["123456789", "987654321"]\n    ```\n\n6. **新增** 按时吃饭小助手全局开关；\n\n7. **新增** 查看群菜单与基础菜单命令分立；\n\n8. **新增** 吃什么帮助文案；\n\n9. **更新** 更新了预置基础菜单~~不想要可以移除~~；\n\n## 命令\n\n1. 吃什么：今天吃什么、中午吃啥、今晚吃啥、中午吃什么、晚上吃啥、晚上吃什么、夜宵吃啥……\n\n2. [管理或群主或超管] 添加或移除：添加/移除 菜名；\n\n3. 查看群菜单：菜单/群菜单/查看菜单；\n\n4. [超管] 添加至基础菜单：加菜 菜名；\n\n5. [超管] 查看基础菜单：基础菜单；\n\n6. [超管] 开启/关闭按时吃饭小助手：开启/关闭小助手；\n\n## 效果\n\n1. 案例1：\n\n    Q：今天吃什么\n\n    A：建议肯德基\n\n    （……吃什么*5）\n\n    Q：今晚吃什么\n\n    A：你今天已经吃得够多了！\n\n    Q：群菜单\n\n    A：\n\n    ---群特色菜单---\n\n    alpha\n\n    beta\n\n    gamma\n\n2. 案例2：\n\n    [群管] Q：添加 派蒙\n\n    A：派蒙 已加入群特色菜单~\n\n    [超管] Q：加菜 东方馅挂炒饭\n\n    A：东方馅挂炒饭 已加入基础菜单~\n\n    [群管] Q：移除 东方馅挂炒饭\n\n    A：东方馅挂炒饭 在基础菜单中，非超管不可操作哦~\n\n## 本插件改自：\n\n[HoshinoBot-whattoeat](https://github.com/pcrbot/whattoeat)',
    'author': 'KafCoppelia',
    'author_email': 'k740677208@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
