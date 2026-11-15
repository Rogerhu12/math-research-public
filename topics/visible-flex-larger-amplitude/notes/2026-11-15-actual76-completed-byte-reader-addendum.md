# Actual76：完整字节读回附记

类型：既有数值证据的字节完整性附记。  
作者：ChatGPT / amplitude。日期：2026-11-15 UTC。

## 结论与来源

第76轮的完整导出原件已由独立只读Actions核验。本附记将五份原报告副本、此前取得的四份相同报告、实际新warm及primary身份回执再次对应。只读结果与正式第76轮的接受步长、最近拒绝和未接受BVP范围一致。未重跑科学，也未增加后继接受门。

原科学run为[43661532089](https://github.com/Rogerhu12/math-research-public/actions/runs/43661532089)，source `1377826d89317b491f75036cafd63c3ea5bea5f1`。原artifact14140726714为640977134 B，SHA256 `b57824ec8cb6ef22525966725fd333c4dfb1a0111aa403ccf54117d02ab7289c`。只读run为[43662815323](https://github.com/Rogerhu12/math-research-public/actions/runs/43662815323)，job132655624114，source `4fcb0ab080482efaf71f8c5cdd2f3358d7b0d820`，全部成功。

根唯一下载其868503 B小artifact14140797850并完成size/SHA/CRC；本地完成标记与digest `351525c97c07a548b4770a0625755108c9c17ac37e5511e3af42c3204c70d33d`对应。本次本地没有重新取得640977134 B原科学ZIP。

完整Actions审计为 `request76-readback/large-arrays/complete-original-byte-audit.json`，795340 B，SHA256 `5d6c7362c914f9c64ce55d160dd555b7b5d07a11b37541d0577b7a0f62df6e2d`。57523 B主摘要SHA为 `73019aa827508c0e1a4ba0c5598fed7fcfdadde9b66cd8cfad837dda185656b8`。本地仅标准库解析、流式SHA、字节相等及整数布局核对，详见[原件对应回执](actual76-completed-reader-addendum.json)。

## 24组查询与完整支持

本轮16组left-RMS和8组原collocation midpoint，各2048角，共49152行。新增的是 **left-RMS485**；原midpoint485仍独立保留，不能将两者混为同一查询。

left-RMS顺序为466、467、468、469、470、471、472、473、475、477、479、480、481、482、484、485；midpoint顺序为473、475、477、480、481、482、484、485。24组679列的局部映射均与原完整索引逐项对应。

声明维数与实际B列并集均为7101，即节点466至486的21份338维物理状态及3个全局control；`zero_layout_nodes=[]`，零布局列数为0。新增left-RMS485复用已有485/486端点，捕获支持未扩大。原C投影仍为4059维修正支持，完整outside offset、完整B和完整H恢复另有各自身份。

实际B模型SHA为 `f74b464eb3fcfe233cc084195e1fed50ab70b52aac07472343c5a96d1d1714d1`。原88次Jacobian调用中仅捕获59、61两批，保存21个唯一端点和21份版本。此处核的是原报告及保存字节，不重新构造Jacobian或证明非线性域有效。

## 已完成的字节范围

| 原件范围 | 完成的Actions读回 |
|---|---:|
| domain NPZ / 内含NPY | 215 / 1396 |
| 完整B、Gamma、Pi拼接 / 全typed beta拼接 | 72 / 1 |
| condensed NPZ / 原数组引用 / 唯一完整数组 | 108 / 42 / 38 |
| 凝聚与恢复raw文件 | 14 / 415120992 B |
| 完整读者实际源码SHA | 71，缺失声明0 |
| 原collocation observer报告 | 11 |
| 原midpoint observer载荷 | 8，均有匹配原descriptor |

domain范围含完整B/Gamma/Pi分块和拼接、beta、mesh、原y/RHS、尺度、中点输入及捕获端点J/P。condensed全部组成部分和引用保留，没有截断basis。14个raw覆盖原g、局部索引、原仿射列及其误差、7101维局部平方根/仿射项/梯度/中心，以及实际恢复向量、恢复右端、局部不匹配和原H残差。

observer账记11次原evaluate、1次原weights、0次observer错误，无额外RHS/J/trial。原实现检查值为adjoint error `3.0483285070092677e-18`、local/full error `0.0`、完整complex-chain relative error `1.4135311081361798e-12`；本附记只读取这些既有Actions数值。

此前primary回执的17项父/报告关系全部为true。其62份源码SHA均与本次71份完整读者清单中的同名项一致；新增9份属于更完整的原件依赖覆盖，不将两种范围混称同一清单。新JSON同时记录原17项、9个新增源名及报告对应结果。

**完整链QR因子原来只在进程内存中，没有导出全部因子数组。** 局部平方根和14个raw审计不等于完整QR因子文件的独立审计，也不等于重新验证完整A/H。保存回执明确保持独立完整因子审计为false。

## 原科学结论与父子身份

status、model、comparison、QP summary、FD五份原报告副本的完整SHA均与原descriptor一致。其中status、model、QP summary、FD与此前公开取件逐字相同；实际新warm压缩字节也单独核对。接受与最近拒绝摘要的原字段逐层对应原trial；摘要为缺失可选字段补的null单独记账，没有当成原始数值。

新warm SHA为 `bba24c1f882d14751c4272148ee0cd6271c584485c6d0d3efaafa1a081a2a97f`，status原解码SHA为 `a1a67b9a1e0e97aa23404a8fa6c5936805de34f763f0076516c4f736aedc4cb5`。其真实父仍为actual74的双SHA和完整producer子树。

原接受步长仍为1/4，原两组完整RMS查询通过；固定本模型权重的merit从43.67031770334245降至43.57938353308094。最近1/2同时出现已建模left-RMS466和原midpoint486失域，原完整RMS及merit未执行，不能称只有一个未建模点限制。原FD四阶误差仍为 `8.532100047207813e-10`，确实绑定新warm，但只检查实际零锚真J定义的affine方程；当前新H没有因此被宣称已有真native解。

`accepted_warm_steps=1`、`success=false`、`new_coupled_finite_acceptance=false`原样保持。本附记补充[第76轮正式结论](2026-11-15-actual-request76-twenty-four-query-quarter-step.md)的完整导出字节范围，不改变同24查询再重线性化一次的后继决定。
