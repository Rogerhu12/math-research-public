# R659：同一闭合候选的完整像握持幅度连续下界

2026-11-20，Astra-larger-resume-24b2ab87-20261120。

**状态：已证明且全体连续位置覆盖实际完成。** 对[R658](R658-complete-body-diameter-and-fixed-grip.md)的同一准确6077闭合C²映射，完整相位像的Hausdorff幅度满足

$$\delta_{\rm hold}\ge{943143\over10^6}=0.943143,\qquad
{\delta_{\rm hold}\over D_0}\ge{943143\over4106819}>0.2296>0.2.\tag{1}$$

目标集合包含全部922径向胞、全部角度、镜像半面和两个平帽；不是核心点位移或开放片距离。这里的Hausdorff量对紧像成立，不以未证明的嵌入为前提。该候选尚无全部等距/嵌入/reach或固定参数精化证据，未标记像的Euclidean商距离仍为零，故本条仅支付一个真实完成指标组件。

## 1. 唯一候选与真实见证点

输入仍是 `curvature-qp-arbitrary-def1-six-step.npz`，SHA256

`607732377449f07611553ebc1ad1e7f2aa20e835d3f613a3018ae56957dd6941`。

准确binary自由系数、派生端口、原$\alpha S+\beta$节点、完整解析lift、同Hold的S/R有理盒和H都与R658完全相同。本条没有变更模型或借用另一候选的直径。

设其未标记完整像为$S_0=A\cup C_0$，A为镜像活动环带，$C_0$为上下平帽。按[R248](R248-finite-C2-phase-family-and-global-reductions.md)的相位公式，$S_\alpha=R_\alpha S_0$。
原准确core接口给

$$r_0=1+\sum_{j=1}^{M}c_j,\qquad F_0(0,0)=(r_0,0,0).$$

取活动像上的真实相位见证

$$p=R_{\pi/2}F_0(0,0)=(0,r_0,0)\in S_{\pi/2}.\tag{2}$$

因为参数圆周作用满射，(2)不需要用“同一材料点走了多远”解释。只要证明$p$到整个$S_0$的距离下界L，Hausdorff定义立即给

$$\delta_{\rm hold}\ge d_H(S_{\pi/2},S_0)
\ge\operatorname{dist}(p,S_0)\ge L.\tag{3}$$

不声称$\pi/2$一定是使完整Hausdorff幅度最大的相位；一个真实相位已经足够给下界。

## 2. 每个连续径向/角盒的准确距离

本次复用R658已经公开的真实位置控制点子程序，只新计算目标距离。
对每个闭原胞，以[R656](R656-fullclosed-continuous-geometry-with-complete-analytic-lift.md)的准确Hermite/Bernstein和角余项得到三个位置区间$X_d$。
在旋转$\phi$正交架中，真实固定p的三个分量为

$$p(\phi)=(r_0\sin\phi,r_0\cos\phi,0).\tag{4}$$

R656严格基本正弦/余弦角盒同时包围(4)，并在相同角盒内向外计算

$$d_\pm^2=\sum_{d=1}^3(X_d\mp p_d)^2.\tag{5}$$

平方区间含零时取下界0，否则取两端平方的较小者，再向下舍入。所有运算逐步向外；丢失位置与p之间的相关性只会使下界更保守。

单个$p$距离不保持所有四分之一圆对称。其在y反射和水平半周下的轨道是$\{p,-p\}$，因此源码对每个角盒同时计算两个符号并取较小下界。这正好覆盖全圆，没有把只对p的四分之一域结果误作全角结果。水平镜像固定$p$，故同一距离界覆盖另一半面。

对闭帽$r\le R,z=\pm H$，准确有

$$\operatorname{dist}(p,C_0)^2=H^2+\max(r_0-R,0)^2,\tag{6}$$

由相同有理输入/向外运算得下界$4.363624078527403$。这大于侧面全体下界，但仍实际纳入最终最小值。

源码逐一返回全部 `cell=0,...,921` 并检查列表完全相等。每piece径向细分数1、全角Q2048（四分之一域513个闭角段），共享闭胞/闭角段包含接缝及所有采样点之间位置。此计算只使用位置，没有不必要的度量正则除法，也不依赖a采样值。

## 3. 新全体实际返回及有理化

全922胞、两帽与镜像的完整执行自然结束，exit0，132.078509322秒。全体距离平方共同下界为

$$B_-=0.8895194323537192.\tag{7}$$

最小盒为胞156、径向子片0、闭角段索引512、witness符号+。邻胞155/157的下界分别为
$0.8895196724559192$、$0.8895211248003735$；其余完整胞并无更小界。

该准确binary64下界经向外平方根给
$\operatorname{dist}(p,S_0)\ge0.9431433784710144$。
另外按Fraction准确核算

$$\left({943143\over10^6}\right)^2\le B_-,$$

故L可取准确有理数$943143/10^6$。配合R658的同一候选完整直径
$D_0\le4106819/10^6$，式(3)即证明(1)。

这一界来自全部闭面位置，未将R645等旧开放prefix见证移用于当前场。R658的D覆盖也未重做；本次只复用其同一位置子程序生成新的全体见证距离结论。

## 4. 固定小标记仍保留同一见证下界

R658已给半径$9/20$的真实固定握持盘，直径$9/10$，并给R650附录C固定标记组件的条件尺寸。进一步设在帽上接任意固定C²图，其竖直高度改变量满足

$$|b_\pm|\le h=1/1000,$$

且仍位于原帽盘内、边界附近有完整零两jet。活动像不改，故(2)仍是新相位活动像的点。
本候选准确$H=8594875381108039/4503599627370496>1$，而$p_z=0$，所以新帽每点都满足

$$|z|\ge H-h>999/1000>943143/10^6.\tag{8}$$

全侧面到p仍至少L，新帽到p至少其竖直距离，故**不必损失h**：

$$\operatorname{dist}(p,S_0^{\rm marked})\ge L.\tag{9}$$

这里只利用具体见证$p_z=0$，不假设整个活动像都处于两支撑平面之间；因此没有绕过R650附录C所指出的全活动slab责任。

R658已证明这种点移动的完整直径预算
$D_{\rm marked}\le4108819/10^6$。所以同一固定标记条件下

$$ {\delta_{\rm hold}^{\rm marked}\over D_{\rm marked}}
\ge {943143\over4108819}>0.2295>0.2.\tag{10}$$

握持直径组件同时为$\operatorname{diam}H_{\rm grip}/D_{\rm marked}>0.219$。
这一具体见证比一般R248的减h稳定性公式稍紧；完整证明已由(8)–(9)给出，不是单凭“小marker”作结论。

本条未实际接上标记，也未宣称其诱导度量等于旧平帽度量。固定帽必须按既有配方选择其自身共同g；含反射Euclidean非全等仍须R625/R238等的全部输入，嵌入/reach仍须全域真实证据。

## 5. 完整来源与执行命令

| 对象 | SHA256 |
|---|---|
| 同一6077 bundle | `607732377449f07611553ebc1ad1e7f2aa20e835d3f613a3018ae56957dd6941` |
| 原同Hold节点报告 | `fc52830031f1fa6ba7e00788d164cefdb88188fc35a56f8dcbab1b1b94012692` |
| 新完整见证距离源 | `2fe486093e3fc41fb87e4f8fc54304f489695449324d84fca1cb7fd9a1520072` |
| 复用R658位置源 | `9085e6713faa1aba1dcc99a0e30ed038f33ca6ec24a2c187e9668a9c4fe26623` |
| 复用R656完整几何源 | `2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377` |
| 原严格FFT/区间核 | `f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d` |
| 本次全922胞见证报告 | `dd58605a12214a97b386693dd018f6bd8ee65c596c463495210f5e4a56f1db97` |

新的小源为 `scripts/resume_20261120/fullclosed_witness_interval.py`。
环境沿R658：Python3.12.14、NumPy2.3.5、单BLAS，IEEE非FTZ向外模型沿R656。
本地真实运行，无另造Actions run。完整逐胞raw只scratch，保留完整源码/参数/父链/报告身份。

令repo为checkout、topic="$repo/topics/visible-flex-larger-amplitude"、work为仓库外重建目录；6077/节点报告的完整重建见R658及所链接v4a父链。

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120/fullclosed_witness_interval.py" \
 --bundle "$work/geometry_path/curvature-qp-arbitrary-def1-six-step.npz" \
 --node-report "$work/fullclosed_solver/data/fullclosed-hold-warm.json" \
 --interval-source "$topic/scripts/parallel_20261117_arclength_interval_positive.py" \
 --geometry-source "$topic/scripts/resume_20261120/fullclosed_geometry_interval.py" \
 --radius-source "$topic/scripts/resume_20261120/fullclosed_radius_interval.py" \
 --out "$work/root/continuous-6077-complete-witness-q2048-r1.json" \
 --angles 2048 --radial-subdivisions 1
~~~

本条完成这个候选的整像幅度下界组件，不把旧单点数值、条件标记或当前约$10^{-2}$的度量残差包装为本课题完成。
