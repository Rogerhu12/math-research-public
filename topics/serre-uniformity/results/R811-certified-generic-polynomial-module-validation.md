# R811：多项式模块的非平凡消去与真实中断续算已验证

日期：2026-11-15。状态：**本篇只记录 generic 模块验证的真实成功。**
它验证原R811后继将使用的同一字段/多项式/完整核/Hermite与续算实现，
不声称原CM曲线的A/B或极除子已经求得。

## 1. 实际公开运行

- run：[43719858329](https://github.com/Rogerhu12/math-research-public/actions/runs/43719858329)。
- job：132829269111，全部步骤成功。
- source commit：3018f7988496be95654cdf16b35192088ae40673。
- 数学测试主进程计时：2.4052703090000023 秒，不含安装。
- python-flint：0.9.0；所有数学均在本公开仓库Actions。

| 固定源 | 字节数 | SHA256 |
|---|---:|---|
| R811_exact_L_polynomial_modules.py | 53397 | 09f21a903e4906666d63f58575b389be7a04c20b68c7fcac624d3821837a9126 |
| R811_generic_polynomial_module_validation.py | 14346 | 7a3b49ea7127b77a253c2e00c2ce1325cdcd75d5a54f1b69479cd7b133265037 |
| R754 原字段adapter | 沿冻结原文件 | f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251 |
| workflow | 3349 | 4b74fd80c89f5310f7a8d05f91a0c7327d3d4e0534cf705f57ebbf9ed2945f00 |
| request | 979 | 4760f21e0775f68b3a97eb00eda1af4fd0938a65a0d8e3023a0a52c94df3e25c |

运行前契约见[原generic验证契约](../notes/R811-generic-polynomial-module-validation-contract.md)。
数学核心、测试对象及真实中断点均在启动前固定。

## 2. 实际数学检查

字段为明确的generic域
$$
L_{\rm gen}=\mathbf Q(c,\zeta),\qquad c^7=2,\quad \zeta^2+\zeta+1=0,
$$
不是原CM参数b的字段。取 $u^2=z$、$\alpha=c+\zeta$，输入
$$
f=\frac{u^2-\alpha^2}{(u-\alpha)^2}.
$$
真实公共因子 $u-\alpha$ 被消去，完整极理想准确为 $(u-\alpha)$。

两图各自完成不可变原 $P=[M_p,-M_q]$、全unimodular列约化、
逆时间左乘原操作恢复完整核、联合H/W的列Hermite，
再对原P核全部 $M_pH=M_qW$。
两个图的H/W均与契约中的手写闭式逐项相等。
两向Laurent包含全过，实际第一图长度1、第二图遗漏零纤维长度0，
因此完整极除子次数为1。

独立的普通字段系数卷积同时通过packed stride13最高c次数12的乘法检查；
Laurent除法确实先消去非单项式因子再判断剩余分母。

## 3. 四种真正进程中断及复原

| 模式 | 首次进程退出码 | 再启动结果 |
|---|---:|---|
| 不间断基线 | 0 | 准确完成 |
| 完成第一个输出tile后 | 97 | 准确完成 |
| 完成操作receipt后、current提交前 | 97 | 准确完成 |
| 原子current提交后 | 97 | 准确完成 |
| cleanup已删除第一个旧tile后 | 97 | 准确完成 |

这四次调用真实的os._exit(97)，没有异常展开或finally清理。
重新启动消费原已成tile/receipt/current状态；不以抛出后正常清理模拟中断。

五份最终数学结果文件各2752 B，全部逐字相同，统一SHA256为
c5cd89b2dd74b02c72b825eb91374d55a3371189cec49ccd2b1c03c5cd61d6eb。
fault模式与路径不属于数学配置，所以这个字节比较确实比较同一数学结果。

## 4. 原artifact与纯IO审读

- artifact：14164256301，serre-R811-generic-module-validation-43719858329-1。
- ZIP：956925 B，共825个文件成员。
- ZIP SHA256：3815dcfb8394798808ac924ed34803a9bc6ea36d7c37ba1bedcb0fa5d818133a。
- 到期：2026-11-16T13:36:22Z。
- 真实summary：3056 B，SHA256 badee1a48d3c860ee25f8ef2c69330479e9e895047a2ff6c5dca8cf51b9acb57。

root已读取实际job日志、原ZIP及summary，核完整ZIP的字节数/SHA，
五份数学结果SHA与四份fault标记，逐项核数学结果直接引用的65个文件spec。
摘要与日志中的真实退出码、边界、源SHA和完成字段一致。
这里没有宣称全部历史已裁剪的大列仍在archive中，也没有重新执行数学。

所有可重算raw/证书只保一日artifact；Git/Release不保存这些数据。
源码、参数、source/run、SHA和本篇实际结论足以定位此次验证。

## 5. 对真实原任务的边界

本次结果支持模块的准确乘法、非平凡极前像、两图相容性和原子续算语义。
原R811仍需真实A/B乘法输出，并保原b字段、完整272维方程和实际两图。
generic次数1、输入α或H/W不能作为原极理想的结果。

R815原导子请求独立运行；本测试没有作为其额外激活门。
原η、原函数DAG、规范高度与Serre主目标均未由此完成。
