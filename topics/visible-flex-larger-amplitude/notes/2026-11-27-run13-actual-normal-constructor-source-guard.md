# 公开13真实入口异常：normal构造的底层来源约束

## RET86：终态导读与完整历史记录

**已知后继终态：** 本文准确定位原 N4096 driver 的旧 schema 字面失配，保完整实际 traceback、pure 缺报告和最小修复边界。修后科学曾运行但未自然返回，run13/14 后来均官方 cancelled；原因未知。[两 run 独立终态](2026-11-27-runs13-14-actual-cancelled-without-complete-science.md)本次保持原字。

本版保留原笔记全部非 JSON 叙述、数值表、公式、时间顺序、来源与参数链接、接受/拒绝及错误/未知原文。1 个重复嵌入的 JSON 改为各自固定全文和精确行号引用；它们的所有原字段、命令、标量、缺值和 whole 身份仍在同一完整旧文件中。这里没有把原 JSON 重编码成数值载体，也没有改动科学源、request、ready、实际输入、checkpoint 或报告。

**完整旧文件：** 24676 字节；SHA256 `558d14fcee888ab7e94dff462e551cdf873b3e61e1783d6e6f8c55cec194ea97`；Git blob `9c580305162154d2430fe1e06840ea26a5820d36`；固定提交 `0ff96dc0001b35cac2301f942e55292fe0f808ed`。[完整旧版](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run13-actual-normal-constructor-source-guard.md)。旧 whole-hash 读者应从该提交恢复原件；当前紧凑笔记有独立新身份，不能冒旧字节。逐块对应与恢复说明见[RET86 完整交付表](../computations/terminal-run10-14-narrative-retention-86-complete-delivery.json)。

下文“当前”“未返”“准备”均保各原节的时间作用域；旧 running 不覆盖已知官方终态。原文所称“以下完整对象”现在由紧接其后的固定完整记录链接承接，不是声称该 JSON 仍内嵌于当前正文。首次准备的 null 也不覆盖后面真正返回的事实。

原始science/pure两次失败已在[前记录](2026-11-27-run13-entry-failure-and-run14-actual-reference.md)登记。现在同一run46028002241/1中两个原异常链读取器均真实返0；这次得到的是原日志中的实际异常，不是重跑求解或推测数值原因。

## 科学入口

原log为6797B，whole SHA256 f1ab18fb5f5da2d736fed5eb0455a5fe61d10261c05511cf3f547ef63bf89887。读取的tail实际包含全日志，第一traceback未截断：

```text
Traceback (most recent call last):
  File "/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_angular_refined_so3_qp.py", line 1094, in <module>
    main()
  File "/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_angular_refined_so3_qp.py", line 544, in main
    q = endpoint.ZeroClosureOperator(base, expected_base_source_sha256=SOURCE_PINS['meridian'][1],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_angular_refined_normal_lift.py", line 257, in __init__
    raise ValueError('This complete normal layer binds its actual independent supported-smooth-triangle base source')
ValueError: This complete normal layer binds its actual independent supported-smooth-triangle base source

```

实际链是driver c64d在main构造q，进入normal2db0的__init__，在实际base source/schema约束抛ValueError。外层launcher的CalledProcessError只是传播此错误，不能拿外层异常代替inner原因。当前证据未单独区分该复合guard的哪一个布尔子句；完整源码定位和最小修复继续，不扩大可接收模型集合。

## 后续纯读取

原pure log1723B，whole SHA2566668fba14c096b42f02dff93c8e11407870885944165c86b2d41283f96074611，读取包含全日志且第一traceback未截断。完整reader在读取实际scientific report时FileNotFoundError；该报告确未生成。没有pure验证成功、完整物理场、accepted方向、final、typed增量或费用结论。

## 两个真实只读返回的完整紧凑记录

> **原 JSON 01：两个实际异常读取器的完整返回。** [固定旧版完整记录，第 30–163 行](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run13-actual-normal-constructor-source-guard.md#L30-L163)。


[完整阶段1–6原卷](https://github.com/Rogerhu12/math-research-public/blob/882086668df076632531f609a83a172dfe75d473/topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46028002241-1-part-001.md)57966B，whole SHA25683cb443967c0c8ec25f8e0cbece736740568fd21e676f85fa8f03a889fb423a0，Git blob c4df0fdbe5de291eb0dcbd74aa2a47b6a5811cc7。原所有参数/command/输出身份仍完整保；两reader从不读科学数组或重算F/J。

继续按本条真实风险修完整normal/base接口和所有受影响的来源闭合，保原目标、全部变量、32normal、预算及完整history。新尝试必须用新的实际输出路径，保原失败报告和日志身份；不会删除guard、替换固定g、缩小参数或增加独立审查/fixture门。J1845只核同一构造约束是否同样受影响；未经证据不泛改。

## 16:24 UTC：完整实际源码给出的确切子条件

实际driver c64d2340fb51d67af98f56e3f6bec136048a43ceb9f7d9bc3ff12dc0b0488d25（95387B，blob726c884ccfa214d62c6846e651ded5beb811ca40）在该调用传：
```python
expected_base_source_sha256=SOURCE_PINS['meridian'][1],
expected_base_schema='complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1',
```
其中source pair本身就是实际3f4d5c0ec5b03eba9e93660e1341c32f1bd4872e0d1250d489894dd4ba6ed915。实际normal2db038574bb13e226b61826949cc66d917f0186fe5b9156a50eb7180da3d4bda（98437B，blobc65014dcebbcc5ccc8949aec47daf50dfbfd99ed）全体具有：
```python
SUPPORTED_BASE_SCHEMA = 'complete-fixed-fejer-angular-refined-supported-SO3-meridian-v1'
SUPPORTED_BASE_SOURCE_SHA256 = '3f4d5c0ec5b03eba9e93660e1341c32f1bd4872e0d1250d489894dd4ba6ed915'
```
base3f的实际SCHEMA与normal常量一致。故复合guard中失败的是driver传入的旧schema字面，而非这两个完整source SHA不相等。最小科学入口修复为把这一字面改成已严格pin的真实N4096 base schema，保normal/base/128个原source pair及所有数值方法不变；需同时闭合新driver的launcher/pure和全部新输出参数。修复未实施前不预报科学成功。

J1845该同一实际调用已由完整driver97ae6ab8、normal543ef572及base78ded268核对：三处schema都是complete-fixed-fejer-radial-bisection-frozen-reference-so3-meridian-with-core-lift-v1，三处完整base source SHA都是78ded2682f5a42bc44a1939e9d814eec17254d1385dfe08a545d6aee109892ef。它不存在这一次N旧字面失配，不据此变更J；此窄范围源码事实不称整族审查通过或科学结果。
