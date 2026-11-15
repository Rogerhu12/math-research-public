# R838：原二阶导数理想的完整认证及最小三阶终止

日期：2026-11-15。状态：**实际准确完成。** 本结果只处理原 $p=41$、原 $f_4$ 与原 $y=y_{f_4}$。新公开计算已经结束；本稿登记原特征零完整 $I_2$、$P_0\notin D$，并由已有逐点公式确定完整原导数理想的最小终止阶恰为3。未计算原 $D$ 的短 RR 坐标、$\eta$ 或规范高度。

## 1. 实际结论和原对象

保持 [R835](R835-certified-original-order4-termination-and-reduced-D.md)、[R836](R836-original-reduced-D-fixed-branch-pencil-and-short-RR-kernels.md) 的原 $Y_L$、原 $L=\mathbf Q(b,\zeta)$、原两图和原 $f_4$。记
$$
\mathcal C_0=\mathcal D_{\rm cusp},\quad \deg\mathcal C_0=20,\quad
\mathcal C=\mathcal O_Y(-\mathcal C_0),\quad
E=(y)_\infty=\mathcal C_0+P_0+3D,\quad \deg D=395.
\tag{838.1}
$$
$P_0=\phi(c_0)$ 始终是原固定点，不换成 R790 的 CM 求值点 $P_1$。R835 已准确证明 $D$ 约化及 $I_4=\mathcal C$。令 $\epsilon=\operatorname{mult}_{P_0}D\in\{0,1\}$，R836 已证明
$$
I_2=\mathcal O_Y(-\mathcal C_0-D-\epsilon P_0),\qquad
I_3=\mathcal O_Y(-\mathcal C_0-\epsilon P_0).
\tag{838.2}
$$
这里 $I_j$ 是原完整理想链，而非某个有限截面子空间。

本次实际计算及下文长度证明给出
$$
\boxed{\epsilon=0,\quad P_0\notin D,\quad
\mathcal J_{2,L}=I_2=\mathcal O_Y(-\mathcal C_0-D),\quad
\operatorname{length}_L(\mathcal O_Y/I_2)=415.}
\tag{838.3}
$$
$\mathcal J_2$ 是原 canonical $B$ 及完整正规基的第0、1、2导数层所定义的真实全局像；它不是提升有限域系数猜出的特征零理想。其原单位选行表达式、原导子和两图齐次化均沿 R827 同一来源。

将(838.3)代入(838.2)立即得到
$$
\boxed{I_3=\mathcal C,\qquad
\min\{j\ge0:I_j=\mathcal C\}=3.}
\tag{838.4}
$$
事实上 $I_2\ne\mathcal C$，因为 $\deg D=395$；又 $I_0\subseteq I_1\subseteq I_2\subseteq I_3$，故更早层不能等于 $\mathcal C$。最小阶结论消费已成逐点公式，没有重新执行第三阶导数，也没有声称单 canonical $B$ 第三层的某个未经另核权框架输出已经计算。

## 2. 实际完成的有限步骤

公开 [run 43771598002](https://github.com/Rogerhu12/math-research-public/actions/runs/43771598002)，job 132988566130；
source f5fa479fd5c3a8bade795906f5bfd2aa23ddc6df。
数学核心运行17.344589635秒，于2026-11-15T22:52:16.012193+00:00结束；运行回执 exit0、error null。

固定原地方的剩余特征 $\ell=1000000753$。原 $\tau$ 图正规基秩272、权 $(0,1^{144},2^{127})$，行权和398。
已成三个原 $C$ 坐标块为
$$
G^{(2)}=[G_0,G_1,G_2]\in\operatorname{Mat}_{272\times816}(k[z]).
\tag{838.5}
$$
原 $C$ 整除、导数和乘回已完成，本次不重做。旧 R835 已成
$$
d_0=\det G_0,\qquad \deg d_0=1320.
\tag{838.6}
$$
本次直接消费完整 $d_0$。唯一新增投影为
$$
V=\begin{pmatrix}I_{272}\\I_{272}\\I_{272}\end{pmatrix},\qquad
d_1=\det(G_0+G_1+G_2).
\tag{838.7}
$$
原权数严格给
$$
\deg d_1\le\sum_c(9+e_c)-398-20=2428.
\tag{838.8}
$$
公开核心准确完成全部2429节点 $z=0,\ldots,2428$，保奇异节点，完整插值并核全部节点乘回。实际得到
$$
\deg d_1=2408,\qquad
g=\gcd(d_0,d_1)\text{ 首一},\qquad
\boxed{\deg g=395.}
\tag{838.9}
$$
扩展 Euclid 的完整多项式乘回通过；没有用抽样或单点秩替代全多项式结论。

原第二图已成证书实际选列
$$
0,\ldots,251;\quad272;\quad345,\ldots,363
\tag{838.10}
$$
给 determinant $695832206\ne0$。这些列全部属于原第0或第1层，因而直接是本次二阶源在 $\sigma$ 无穷纤维的满秩见证。原 $P_\sigma(0)\ne0$ 也已认证。本次只读原列号和 determinant，不重新计算第二图或 minor。

## 3. 全图长度和特征零相等的证明

令 $\Delta$ 为(838.5)全部272阶子式的首一 gcd。Smith 正规形给
$$
\operatorname{length}_k\operatorname{coker}G^{(2)}=\deg\Delta,
\qquad \Delta\mid d_0,\quad\Delta\mid d_1.
\tag{838.11}
$$
故 $\deg\Delta\le395$。原 $C_\tau$ 的 determinant 为真正20次多项式，于是
$$
\operatorname{length}_k\operatorname{coker}(C_\tau G^{(2)})
=20+\deg\Delta\le415.
\tag{838.12}
$$
额外同源齐次列只缩小余商；(838.10)覆盖补点，所以特殊纤维整个余商长度至多415。

准确包含为 $\mathcal J_{2,L}\subseteq I_2$。特征零目标余商长度由(838.2)给出 $415+\epsilon$。在原 proper 模型上取 $\mathcal Q=\mathcal O/\mathcal J_2$。至少一个非零子式及第二图满秩使特殊纤维支撑有限，泛纤维支撑也有限；该 proper 支撑对原 DVR 为有限，推前是有限模 $M$。有限 DVR 模结构定理直接给
$$
\dim_{\operatorname{Frac}A}(M\otimes_A\operatorname{Frac}A)
\le\dim_k(M/\mathfrak p M).
\tag{838.13}
$$
不需预设余商平坦。因此
$$
415+\epsilon
\le \operatorname{length}_L(\mathcal O/\mathcal J_{2,L})
\le415.
\tag{838.14}
$$
故 $\epsilon=0$ 且两长度相等；$I_2/\mathcal J_{2,L}$ 长度为0，包含就是相等。这证明(838.3)，(838.4)随即成立。

完整一般方法和原整来源见
[原二阶长度方法](../notes/R827-original-order2-colength-and-complete-I2-certificate.md)，
SHA256 e78882103376e39aa71b94e64a839c3c81971705b68789c1bf6dc6f3a83425e7。
本次真正新数值输入是(838.9)；不把有限投影未消去的因子反向认作真实支撑。

## 4. 运行、成果和来源身份

下列机器产物仅留于一日活跃 artifact；Git 保存简明账本、脚本、参数和证明。

| 对象 | bytes | SHA256 |
|---|---:|---|
| 最终证书 | 6368 | d9674a457419bb27480e791e0c3956cfec71dca63471bd446da0fc9dc21ef36b |
| 完整 outputs manifest，2456项 | 424978 | 6b8d5c0138b2d42c323093e05f73e418ea298c7f791f148fc6ea1cb65bd413f3 |
| manifest reference | 227 | 2accc9e9dfed6f9351c62c91be3868d39c4000d649556da687e402e3bc38fb2d |
| 完成 stage manifest | 109039 | fef4d4afb62aa189546bc7891644c8c941667333b0caac3d2d4a32874d8f6542 |
| 两 determinant 的 gcd 与长度证书 | 19884 | 3acff169eefd6f7822d7a3266752cfc475e741642541d259af498c36fc5f1c8f |
| 新完整 determinant 多项式 | 15054 | fead6e58cfe8fad26a24608385f0292643177c948a564e57a71628af2e2d3526 |
| 全2429节点索引 | 108317 | 958cd523bea3654c596fe9faef320c51398c2e63e653cbe73ea04f2f384081fa |
| 原已成列接口 | 2636 | fd940bdf627962077c6b7cc91a3ee26ac3137a0f5440fb6d90d3bb9a9f9fbb58 |
| 核心回执 | 477 | 78e0965a7fe7868a50e9627f2f174d9fdcd318bf0857cfa851557f295d741a27 |
| 运行回执 | 443 | 564957f6f8d9ef4b40dc06cea0366ef624eb45f5a9111a929401d8d2b88adbfd |

stage manifest 登记2447项，包含阶段目录本身；完整输出为2456项，ZIP为2458成员，不能混用计数。数学配置 SHA256：
d48177b1e1ec9f93db8ac4214c9ac20edf78afcda2cc5bbfd05f69ced1bcbf05。

| 生产文件 | bytes | SHA256 |
|---|---:|---|
| scripts/R827_order2_colength_certificate.py | 32361 | 7a6d64aa30fbe78282cdc79e00407e2267ebcaa053b030b899c5a253188e48d5 |
| scripts/R827_order2_colength_public.py | 33155 | f42e96fc9397afddbff16d70dc804072c6a337cc124c4da61ddd32db8254bfb5 |
| 本次 workflow | 5887 | af8057db52ed30a52643b79f3e138c5ed9ff26cf7ceaf7b75900a3fd539693da |
| 本次 active request | 5048 | d35b8ca4738f58e33825d2aff853e73584a0e7cb389bdd9cb5a193250a7941b5 |

artifact 14184482549：
serre-global-R827-order2-colength-43771598002-1，
37939300 bytes，ZIP SHA256
6f063bc0cc2b2a121e2d048002fbc394b4414ef1c790c6d58267af7ca4a77f1e；
到期2026-11-16T22:52:19Z。

| 当前所需载体 | bytes | SHA256 |
|---|---:|---|
| R827-determinantal-completed-source.tar.gz | 27499704 | eb908748fed6d68e49656f8df9f65212f849a2ffee672bf792eb63a2fd082962 |
| R827-order2-retained-R835-source.tar.gz | 459342 | 826c2f4e265c733547d15fa0111f3dd95791cb8fdb9f8df59436af45156aa301 |

第一包保原五层完整 C 坐标，本核只用前三层816列。原233593489 bytes 上游全输入载体仍在 R835 artifact，不能虚构它已包含于此小包。

本地结束后仅做纯 IO：15个小件含 manifest/reference，12次 Range，共1825000 bytes；13个非 manifest 小件共282796 bytes。读取核对真实 run/core/final、完成状态、文件 SHA 和字段；未在本地执行新数学、重跑节点或下载矩阵系数。

## 5. 下一子问题的准确入口

原 $I_2$ 现在有 canonical $B$、全部正规基及前两阶导数给出的完整特征零生成表达式。结合 R837 已成共同零恰为 $\mathcal C_0+P_0$ 的两锚，
$$
I_D=(I_2:I_{\mathcal C_0+P_0})
\tag{838.15}
$$
已有固定准确原源。

仍须在所用权次取得真实全局截面秩或准确包含；层的全局生成不自动等于任意低次数的截面满射。后继单位选行 solve 可定义真正特征零对象，不能将未经提升的模核称为准确坐标。本结果不填写295条 $H^0(3H-D)$ 基，不填写其他五个 $\eta$ 的终止阶，不填写原主函数、规范高度或全 $p$ 一致性。主目标继续依 README 研究。
