# 接手后的旧运行结果与 P 完整认证实现

日期：2026-11-20；会话 Astra-rank2-Sha-resume-08eb2b79-20261120。

## 1. 亲读完整旧日志所得事实

以下六个旧任务均已结束，退出码 137，尚无完整末端 PASS。
不能把退出码本身解释为数学反证或已确定的内存耗尽。

| run / job | 最后已确认阶段 | 原日志 SHA-256 |
|---|---|---|
| [43866568746](https://github.com/Rogerhu12/math-research-public/actions/runs/43866568746) / 133296518979 | tate19: actual eta48 U recovery | `ec777ec4e931eacb323e9965ceb07adec2920b062fac71f68b3a2af686b6bf78` |
| [43901392214](https://github.com/Rogerhu12/math-research-public/actions/runs/43901392214) / 133418654415 | persistent PARI basis expansion ready | `75d79d749bb8d5c957fff37ae3f18a17af9f247f2874d449e30217282f47e24c` |
| [43903661921](https://github.com/Rogerhu12/math-research-public/actions/runs/43903661921) / 133426625444 | persistent PARI basis expansion ready | `3db4df27bc53dd7048b1830249cba22a1c3b14576b3f4a7bac2435b0fd310346` |
| [43913500850](https://github.com/Rogerhu12/math-research-public/actions/runs/43913500850) / 133461459569 | r910: single original field inversion start | `96d386d8e57e74a2024e18ef10aead9b893667695e0cc14f160789feece93516` |
| [43922594376](https://github.com/Rogerhu12/math-research-public/actions/runs/43922594376) / 133493496664 | r919: single original field inversion start | `2ac147962b1f204fae1fc0340f6acbc527ce3f6b4aa693166e602ade41f81a97` |
| [43924337986](https://github.com/Rogerhu12/math-research-public/actions/runs/43924337986) / 133499674320 | r919: generic separability certified by specialization | `d2ad2c7da553a514119cb7ed0d111fa2315569faf665ee07cfd6bbf90c8a24b6` |

两条 P 路径分别在 ℓ=1000000033/N=256 和 ℓ=1000003/N=512 完成
全部1226行模素数幂检查、三根合成、有理重建及原初始展开，得到同一坐标 hash
`358238d2595ab4e7873fa41729e725528ab3904cc803d5d1aca22ce010e7be67`。
其后扩展同一 PARI M2 基到4287项，日志确认扩展完成；没有后续完整恒等式回执。
R910/R919 已完成一次关系及两系数的48次模约化，最后停在单个原函数域逆元。
geometry-first 最后仅确认可分特化；不能登记正规化或 RR 完成。

## 2. 同一个 P 末端的等价精确实现

`original_cubic_q_certificate.py` 用
$$
A_N=\mathbb Q[q,a]/(q^N,a^3-17),\qquad N=612(k+1)+3
$$
表示原三次域截断级数。基 $1,a,a^2$ 自由，三条有理多项式全部为零
当且仅当原级数为零。因此它仍逐项认证原 $0\le j\le612(k+1)$ 全窗。
若 $x=\sum x_i a^i,y=\sum y_i a^i$，令
$d_i=x_iy_i$、$e_{ij}=(x_i+x_j)(y_i+y_j)-d_i-d_j$，则完整乘法为
$$
xy=(d_0+17e_{12})+(e_{01}+17d_2)a+(e_{02}+d_1)a^2.
$$
所有乘积在有理多项式 FLINT 后端精确执行并模 $q^N$，不作浮点或模素数替代。
$\theta=q\,d/dq$ 保持理想 $(q^N)$，所以各步截断不损失末端系数。

同一完整 PARI M2 基的高展开逐一匹配全部旧低展开；每个已选乘积的全部旧
低前缀也直接复乘检查。对一组乘积按共同前缀分组，准确使用
$\sum c_{ijk}g_i g_j g_k=\sum_{ij}g_i g_j(\sum_k c_{ijk}g_k)$；
低权的相同公式适用。内层统一清分母后以整数多项式求和，最后准确除回。
因此 A、B 仍是原已重建的两个模形式，不需要存储完整高阶乘积矩阵。

原两项 cusp 支通过 $\operatorname{ord}B=e$、$\operatorname{ord}A=e-1$ 和
$$
y_{-1}=A_{e-1}/B_e=-1,\qquad
y_0=(A_e-y_{-1}B_{e+1})/B_e=-(v_{new}+3)/2
$$
逐项检查，初始13项的原独立检查继续保留。随后原
$$
C=(\theta A)B-A\theta B,\qquad h=qf^3,
\qquad C^3-hA^2(A+v_{new}B)^2B^2=0
$$
在完全相同的 $0..4284$ 范围精确认证。采用
$A^2(A+vB)^2B^2=(A(A+vB)B)^2$ 仅为结合律。
原 u、λ、vnew、全部CM系数、权/维数、三根、全部原有限行和整返回17均未改。

这里已证明的是实现与原认证等价；新运行尚无 PASS，尚不能声明 P 已认证。
后端表示依据 Sage 官方
[有理多项式 FLINT 文档](https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_rational_flint.html)。
共享文件仅改本题 `.github/workflows/rank2-sha-original-P-small-prime-dixon.yml` 的
依赖/触发清单，确保新 helper 存在；仍只在公开 Actions 做数学执行。

## 3. 真正规化的依赖拆分

第七个旧任务 R922 run43927286602/job133510000884 同样以137结束，
最后确认原eta48可分特化，未到 U 的最终恢复。完整日志hash
`19fc4d5c1e35ffd770568e38e3de55feb902a0b6eaa16d025e3c14b3b1414c04`。
逐行检查旧geometry-first函数可见，它仍先建立原48次域的
$dT/dt$ 及 $a_t=-T/(24t\,dT/dt)$，之后才调用 quotient_divisors；
因此其“最后可分特化”的日志不表示正规化算法已经运行。

新 `produce-original-quotient-geometry-only.py` 直接由同一完整Tate方程
建立同一个24次域 $D=\mathbf F_{29}(s)[L]$，立即调用原
`quotient_divisors`；该函数只读取 D,s,L，逐字保留全部九尖点、
Au、Av、branch、D0和canonical degree的检查。这是可精确验证的依赖拆分，
没有替换几何对象或下游条件。它只报告原商的正规化/除子结果；
U、eta48坐标、完整RR基、两原映射和shadow仍分别需要原有认证。
新本题workflow为 `.github/workflows/rank2-sha-original-quotient-geometry.yml`，
使用同一固定Sage镜像、prime29、原q4500/trace170方程；不保存重算输出。

首quotient-only run44712364182/job136206970253已完成同一Tate方程认证，随后因调用者把原4返回值误读为2而退出。已按原函数return k,Ks,polynomial,result修复，数学输入/条件无变。完整原日志hash0eb8ba7926a54d6f84be6e610a379c040a1a8bcae616e6eea342d22e3a6d3ce4；此失败不提供正规化结果。

## 4. 固定 Sage 10.6 的构造接口修正

2026-11-20 新P run44711820528/job136205139671/source7dd40baad2aea0abe82867420d30ca7cac8e381a 在974.39秒再次通过全部1226行、3168个有理坐标重建和原短支，坐标hash仍为358238d2595ab4e7873fa41729e725528ab3904cc803d5d1aca22ce010e7be67。随后固定镜像在 `PolynomialRing(QQ, "q", implementation="FLINT")` 抛出 ValueError，尚未执行新高阶认证。

修复使用该版本默认的 QQ 多项式构造，仍断言实际类型来自 `polynomial_rational_flint`；整数后端不变。将构造、统一清分母和截断微分的API检查放在CM输入及Dixon重建之前，失败将立即显现。这个失败是接口兼容问题，不提供数学反例或完整映射认证。

09:49共享执行环境失联。此前全部工作已推送；此后使用已授权的GitHub接口读取当前main、核对两README、创建以最新main为父的原子提交并以expected head非强制快进更新。冲突时重取最新main及原文件后重新合成，绝不覆盖他人提交。通过仓库既有 `rank2-sha-readonly-rule-pull.yml` 请求真实部分克隆/pull和README差异；回执未到之前不把接口读取记为实际git pull。

只读run44714703291/job136215000894回执确认：09:54:55 UTC实际稀疏clone/pull成功，head b688d6ac703fec422a7c864bcdc997cc553185fd，相对6de107b037d8e4811340ec6dcc784a4e1f7746c9两README无差异；根blob282e86b03385d3b6245ce7100ae2e2af7b103c2d，题blob965ab236bbd6753acb812b45fcc36ae9b6f83b3c。完整题库存34,784,075B/2580文件，无单文件超5MB，三个既有旧输入块未改。共享环境随后恢复，本地再次实际pull至ba6fe7a25b83322caa21ba1bc11ba31e52002127并核对两README仍无差异。P修复后run44714703201/job136215000168，商正规化run44713040079/job136209307176仍在运行。

## 5. 原中间坐标的局部商恢复与全局验真

新增 `original_tadic_quotient.py` 及 `produce-original-middle-tadic.py`，另以本题
`rank2-sha-original-middle-tadic.yml` 在同一固定Sage镜像执行。这不是另换函数域：
仍使用原Tate认证的24次式，以及原
$$
H(t,X)=X^{24}p_t(X+729t^{12}/X),\qquad \deg_XH=48.
$$
原R922 primitive relation经同一48次模约化得到 $A,B_0$；精确待解式为
$$
A U=-B_0t^{12(s_A-s_B)}.
$$
所有右侧尺度均在局部恢复前放入，避免先恢复一个额外带大单项式的商。

### 局部计算的正确性

记 $K=k(t)$。选择一个有限常数扩域 $k'/k$ 中的 $c$，要求所有原系数在 $c$
正则，且 $A(c,X)$ 在 $k'[X]/(H(c,X))$ 中可逆；后者以完整扩展Euclid等式检查。
令 $z=t-c$。因 $H$ 首一，
$$
\mathcal A_N=(k'[z]/z^N)[X]/(H(c+z,X))
$$
在 $1,X,\ldots,X^{47}$ 上自由，且截断映射相容。已知模 $z^n$ 的逆元 $v$ 时，
$$
v_{2n}=v(2-Av),\qquad 1-Av_{2n}=(1-Av)^2
$$
给模 $z^{2n}$ 的逆元。实现仍对每一次提升的全部48个坐标检验 $Av=1$。
这一步只在有限精度的原代数中执行，未调用原 $K$ 上的大Euclid逆元。

对商的48个坐标分别作有理函数恢复，明确检验分母在 $z=0$ 非零及恢复同余。
平移回 $t$ 后将分母化为首一，并检查全部分子/分母系数被 $x\mapsto x^p$
固定；因此候选确实下降到原 $k(t)$，不是留在新的常数域中。

### 有限精度不作为完成判据

候选在原 $K[X]$ 中清分母。设清分母的式分别为
$A=A_0/d_A$、$U=U_0/d_U$、$B=B_1/d_B$、$H=H_0/d_H$，所有 $d$ 非零。
精确检查
$$
R=A_0U_0d_B-B_1d_Ad_U
$$
被 $H_0$ 整除，使用完整pseudo-remainder及其乘回恒等式。因为 $d_H$ 在 $K$
中可逆，这恰是原代数中的 $AU=B$，没有以局部模 $z^N$ 为零替代原恒等式。
若检查失败则提升精度；4096只是本次资源上限，耗尽不证明商不存在。

最后还必须逐字通过两条完整原 $\Phi_{17}$ 方程、$U\ne T,V,0$ 及两个原
Atkin等式 $W(U)U=W_3(U)U=729$。因此即使primitive relation只提供候选，
也没有省略原始唯一中间点的最终认证。

### 原绝对Atkin作用及不必要逆元的消除

由 $H(T)=0$ 和 $H(0)\ne0$，直接用
$$
T^{-1}=-\frac{T^{47}+H_{47}T^{46}+\cdots+H_1}{H_0}
$$
取得同一个 $T$ 的逆元，只在基域除以 $H_0$；不触发48次域Euclid。
原 $a=729t^{12}$、$\iota(t)=1/t$ 下，逐系数精确验证
$$
X^{48}H(t,a/X)=H_0(t)H(t,X),
\qquad
X^{48}H(1/t,729/X)=H_0(1/t)H(t,X).
$$
故 $W(T)=a/T,W(t)=t$ 与 $W_3(T)=729/T,W_3(t)=1/t$ 都是同一原代数的
实际作用，并保留旧 $T,V$ 的四个端点等式。它们的平方及交换性直接在
$t,T$ 两生成元上成立，不另选根或相位。U的两个完整Atkin等式仍独立检查。
本producer不需要 $dT/dt$ 或其逆元，因此不为一个U-only证书计算该RR数据。

以上是恢复算法和原证书的等价性说明，**尚无本次U运行的PASS**；
商正规化、完整RR、闭点、两原映射和shadow各自的缺口不因此消失。
接口查照Sage官方[有限域多项式文档](https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_zmod_flint.html)
及[有理恢复定义](https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_element.html)。
