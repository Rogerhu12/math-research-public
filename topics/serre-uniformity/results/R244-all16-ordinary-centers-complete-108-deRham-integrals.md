# R244：16 个非 CM 普通中心的全部 108 个实际 de Rham 积分

## 1. 完成的数据与范围

本条完成并封存以下全部 16 个普通中心，统一采用 R231 的真实
73 坐标和原参数、基点 $C=P-b$，每盘保存 54 个全纯积分及 R240
的 54 个第二类积分，均精确到 $47^4$：

$$j\bmod47\in\{1,5,7,11,12,15,19,24,27,28,30,32,41,43,45,46\}.$$

总计 $16\times108=1728$ 个实际标量积分以及各盘的 54 个 Hecke
循环坐标模 $47^3$。最后的 j01 已完成原长链的保主函数重演，
与此前 R304 使用的纯 Abel 运算在全部 54 个全纯积分、全部 54 个
循环坐标和实际终点 SHA 上逐项相同。

总文件 p41_all16_ordinary_deRham47_complete.json.gz 的 SHA256 为

~~~text
db72c9640796891ff292e3cb610e832cb1f3e95fafad8f5402af9bf534edcdfd
~~~

三个 CM 普通中心由 R256 另外封存。因此全部 19 个普通中心的
这 108 个积分现在都有真实完整证书。本条没有把此事实当成局部
规范截面高度已完成；普通各盘的真正高度与根检验仍由它们各自的
结论负责。R304 的全 129 盘、53 个全局多项式也不重复登记于此。

## 2. 原始大倍数链和完整主函数

对每个真实基点类执行原冻结 R241 原生精确线性代数的 Makdisi
群链，采用同一个 304 位乘数

$$m=21113421681728164076758160383370947105909472013138012462421148345826995695660466565589785072.$$

每盘 454 次实际 AddFlip 操作，每个输入输出点、标量系数、加倍或
相加关系、V3 真主函数及原空间基均保留。初始负点函数以及两个
formal extraction 函数一并保存，共每盘 457 个实际函数。16 盘
合计 7264 次长链操作与 7312 个保留函数；并非只有数值日志或
末端抽象 Lie 坐标。

各盘完整归档已随其独立七输入清单交付，包含 459 个文件成员。
R244 聚合以各盘实际 Abel/第二类证书 SHA 为边，不复制或修改
这些先前冻结数据。长链中断后由原前缀检查点恢复，未把未执行
后缀记为完成。最后 j01 的重新运行还与原纯 Abel 终点完全相同。

## 3. 从真实终点到第二类积分

R248 的短运输把实际终点 $D_{\rm final}$ 送到 R141 family1 的
真实微小除子 $A_1(t)$。完整参数、有效点、Frobenius、145 阶交空间
单位子式和 $820\times73$ 主理想运输均保存。

准确短函数为

$$\phi_{\rm short}=(v_1/f_0)(F/G),\qquad
\operatorname{div}(\phi_{\rm short})=D_{\rm final}-A_1(t).$$

其中 $v_1/f_0$ 的基截面尺度必须保留。对原 R240 微分 $\nu_j$，
在实际 family2 点计算 $d\log\phi_{\rm short}$，得到

$$\int_{D_{\rm final}}\nu_j
=\int_{A_1(t)}\nu_j+d\log\phi_{\rm short}\big|_{P_{2,j}}.$$

原长链累计函数按真实输入输出符号满足

$$\operatorname{div}(f_{\rm final})
=D_{\rm final}-\epsilon m(P-b),\qquad\epsilon\in\{1,-1\}.$$

全部 455 个参与长链校正的实际函数在 family2 的 54 点为单位，
每一步由真 V3 系数求 $f'/f$，同时核对 Frobenius 协变及完整标量
DAG。故

$$\epsilon m\int_{P-b}\nu_j
=\int_{A_1(t)}\nu_j
+d\log\bigl((v_1/f_0)(F/G)\bigr)\big|_{P_{2,j}}
-d\log f_{\rm final}\big|_{P_{2,j}}.$$

m 为 47 单位，最后准确除去 $\epsilon m$ 不丢精度。这里采用真实
主函数范数的对数导数；没有从全纯积分或抽象群矩阵推测第二类
积分。全部终点和长链校正已经执行，所有 16 个完成标志均为真。

## 4. 独立汇总审计和 j01 的最后闭合

新标准库检查器逐盘验证聚合与真实 Abel、第二类证书的 SHA 边、
54 个全纯值、54 个第二类值及循环坐标；并直接重算上节所有
$16\times54=864$ 个终点/短函数/长函数恒等式的实虚两部分。

j01 的保主函数重演输出与先前纯 Abel 输出在以下三项完全一致：

- canonical_log_C_mod47four 的全部 54 值；
- actual_center_C_cyclic_coordinates_mod47cubed 的全部 54 值；
- actual_multiple_point_sha256 的完整实际终点。

原纯 Abel 与新保函数版的外围文件 SHA 可以不同，因为后者绑定
完整运输数据；上述实际数学内容与终点严格相同。故 R304 已发布
的全局多项式不因该后续保函数重演而改变。

此独立审计只重算必要的聚合恒等式，并不声称重新执行 16 条长链。
真实群链、RR 终点、全函数导数由冻结生产执行器实际完成；其
每盘证书和原始归档均可重建。

## 5. 文件及复现

完整输入、字节数、依赖及源码见 R244-handoff-manifest.json。
聚合 complete 文件与最后实际 checkpoint 字节一致，16 盘齐全，
remaining_disk_ids 为空。校验入口可直接对仓库发布数据运行：

~~~bash
PYTHONDONTWRITEBYTECODE=1 python scripts/verify_all16_ordinary_deRham47.py \
 --aggregate scripts/data/p41_all16_ordinary_deRham47_complete.json.gz \
 --abel-dir scripts/data --second-kind-dir scripts/data \
 --old-pure-j01 scripts/data/R304_pure_Abel/ORD_j01_Abel47.json.gz \
 --output /absolute/path/to/R244-all16-deRham-independent-audit.json
~~~

所有生产源继续采用 R241/R248 已冻结版本；本条新增最终聚合与
独立检查器，未改旧核心或重复声称后续局部高度、全局统一性定理
已经由这些有限数据完成。
