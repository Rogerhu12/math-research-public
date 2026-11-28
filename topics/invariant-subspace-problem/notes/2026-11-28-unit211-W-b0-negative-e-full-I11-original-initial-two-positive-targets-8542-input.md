# W/b0 的 (-1,0) 射线：十一条完整原式与两个固定正幂目标

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28。GPT-6 Astra Pro（AI-assisted）。

**状态：新的首次输入，尚未执行。** 本输入在旧完整七式的同一点参数上加入四条完整原值条件，重新构造十一式的全部最低项分区。只在实际返回十一源 Laurent 组合后，才记录单位排除或目标正幂。旧七式算法、旧投影、旧首项分区和旧返回均不重跑。

## 1. 固定作用域和来源

使用当前已付原条件的 W/b0 物理图。此处原值差判别量 $D\ne0$ 是已有物理作用域；它用于解释低 D 次原值条件的必要性，**整个新计算从不求 $D$ 的逆**。

原七式定义直接来自：

- 原源 blob b33c1abc4ebeaf2ad7f84ff883a56155352df81e，SHA256 54e04e96a39f0caca9e59d55ba3636f27cf8678c7cfeffbecb6212ce8756af0d；
- 源名 2026-11-28-unit211-W-b0-negative-e-full-I6-q2-original-initial-t-valuation-8542.py；
- 其唯一实际 run46160462146/job141026414218，仅完整七源首项返回，未关闭 (-1,0) 射线。

只沿既有原 q2/R6/N5 首项结论（run46157115224）已经限制的分支：
$$
v(e)<0,\qquad v(k)=0,\qquad \lambda\ne0,\quad v(\lambda)=0.
$$
固定 $p=1009$。不扩大到其它五条仍保留的权射线，不重新执行旧 q2/R6/N5 首项输入。$t$ 的全部有理相对估值和 $t=0$ 分开保留。

四条新值式引用完整已刊身份：

[原个别 N/P 和完整 NV 的低 D 次压缩](../results/R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)，blob f4e6d79b9956e5a8b39e4a4f88bfbe17eee945f0。

[一般缩放 N4 的完整三个系数](../results/R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)只说明三个 Z 的完整原来源；本源直接在新的同一点 Gram 上计算完整 N4 和极化，没有从 W 特殊分量反定义 NV。

## 2. 同一点完整原 Gram

系数环为 $\mathbb Q[e,k,\lambda,t]$ 的既有权局部化。令
$$
u=e+1,\quad Q=ek,\quad \bar V=uk+2,\quad
\delta=1-Q,\quad
\ell=\frac{u((k+2)^2-2ek)}{k\bar V},\quad m=u-\ell,
$$
$$
M=\ell(2u-\ell Q)-u^2,\quad bc=\frac{M}{4\delta},\quad
T_0=2u-\ell Q-2u^2,\quad J=2u(1-u)+\ell Q,
$$
$$
\Phi=T_0+4u-4+Q,\quad P_f=T_0(J-Q),\quad
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3.
$$
整个 b0 图的已付参数 $A_*=4uQ-J$ 给
$$
\kappa=\frac{uQ\ell}{A_*},\quad T=\kappa(2\lambda-3),\quad w=\lambda-1-T,
$$
$$
P_ff+QP_{02}(\ell+T)-(\lambda P_{02}+eT_0)T_0+bcQ\Phi t=0.
$$
随后
$$
V=\frac{Jf-\lambda P_{02}-eT_0+bcQt}{Q},\qquad
W_1=T_0/2+2uf,
$$
$$
x=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},\qquad A_1=2f-2V+2bc t.
$$
在 $\rho^2=\delta$ 中恢复 $p=1+\rho,q=1-\rho$、$b=\ell/2+m\rho/(2\delta)$、$c=\bar b$、$X=x+\rho y,Y=\bar X$，以及原四行
$$
g_0=(0,0,p,q),\quad g_1=(0,A_1,r,s),\quad
g_B=(p,r,0,t),\quad g_C=(q,s,t,0).
$$
其中 $r=X-(1-\ell)p-ct,\ s=Y-(1-\ell)q-bt$。

真 double-germ 乘法的第二分量始终为
$$
(vz)_1=v_0z_1+v_1z_0.
$$
原 E1 独立构造；不使用曾有定义错误的 compact 平方，不偷换 E1 与加权 singleton 均值。原七式是
$$
E1,\ EBe,\ EBo,\ N1,\ NS,\ PS,\ q_2.
$$
$q_2=2\,ad/\ell$ 沿已刊整 b0 原 q2 的必要性保留；没有把它当作仅均值系统的充分条件。

## 3. 四条真正新增的完整值条件

记
$$
A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_\lambda-T^2,\quad
K=\ell^2B_\lambda-3\ell TA_\lambda+2T^3,\quad
A_0=(\ell+T)/\ell.
$$
原单点值按同一 $\rho$ 分解为
$$
N_4(g_B)=N_a+\rho N_b,\qquad
P_2(g_B)=P_a+\rho P_b.
$$
新输入精确使用
$$
R_6=MK^2-4m^2D^3,
$$
$$
N_{\rm low}=DN_b+
2\lambda P_{02}\left(\frac{KA_0}{m}+\frac{2mD^2}{\ell M}\right),
$$
$$
P_{\rm low}=DP_b+P_{02}\left[
\frac K{2m}\left(3A_0^2+
\frac{(3m^2/\ell^2+\delta)D}{M}\right)
+\frac{6A_0mD^2}{\ell M}\right].
$$
完整值向量的两个方向为
$$
V_0=(1,w,A_0,A_0),\quad
V_1=(0,0,m/\ell-\rho,m/\ell+\rho).
$$
同一个原 N4 定义给
$$
Z_0=N_4(V_0),\quad Z_2=N_4(V_1),\quad
Z_1=N_4(V_0+V_1)-Z_0-Z_2,
$$
$$
V_{\rm low}=DZ_0+\frac K{2m}Z_1+\frac{D^2}{M}Z_2.
$$
三个 Z 的奇部必须实际为零；两个原向量的迹分别为 $\lambda$ 和 0。这是完整原二次型，没有用某个 N4 分量或 $\Phi$ 倍数替代。

分母只用原图已经支付的权因子。程序逐次剥除的标签为
$$
e,k,u,\delta,\bar V,k+4,P_{02},M,k+2,\ell,m,
2\ell-1,A_*,P_f,\Phi.
$$
这里只是这些既有单位的多项式分子支持；它们不是新的首项单位。尤其 $k+2$ 在原点非零，**不代表其估值首项非零**。

原低 D 恒等式
$$
N_4(DV_{\rm val})=D\,V_{\rm low}+
\frac{Z_2}{4m^2M}R_6
$$
及两条个别奇部身份给四新式在当前物理图上的必要性。新构造只正乘 D；在任何首项 cell 中，不删除 D 首项零面，也不倒任何范数或新的几何头。

## 4. 十一式的新最低项分区

每条原有理式 $F_i$ 先清其**完整既有权分母**，再只除已付权内容和非零有理常数，得到整数本原多项式 $\widehat F_i$。程序完整返回
$$
a_i\widehat F_i=b_iF_i
$$
及两边的所有系数，$a_i,b_i$ 仅为旧局部化的单位。零式保留为零，不伪造新约束。

新最高几何次数上界依次为
$$
(2,2,2,2,3,3,2,6,5,5,5).
$$
这只是完整展开后的检查；全部实际次数和 SHA 以唯一首次输出为准。

归一 $v(e)=-1$，令 $\tau=v(t)/(-v(e))$。对每一个整数项
$e^ik^j\lambda^lt^r$ 使用几何权 $-i+r\tau$。**从全部十一式重新求下包络断点**，再枚举所有开区间和所有断点，不预设还是旧五个 cell。$t=0$ 先原式专门化后另作最低项。

某最低面的系数全被 1009 整除时，该 cell 完整保留，不擅自提升到另一层。只要最低面有一个 1009 单位系数，所有其它项的几何权严格更高，且整数系数 p 估值非负，所得模最低式就是必要原条件。e 的非零首系数可在代数闭剩余域通过统一参数缩放归一；k、lambda 和非零 t 的首系数保留为三个 Laurent 变量。

## 5. 新十一源 Laurent 组合和固定目标

每个 cell 的输入为全部十一条必要最低式。只在非零 t 的 cell 中允许三变量 Laurent 单项式；$t=0$ 中所有式和全部乘子不含 t 逆。

程序以四条新值式优先，固定种子次序为
$$
(7,8,9,10,0,1,2,3,4,5,6)
$$
（从0编号），随后一次运行新的十一行 Laurent 行算法。旧七式的独立算法不执行，也不以其结果作为本次门。

每一次行约化、S-pair 和 Laurent 单项式约除都附十一维来源向量，并逐多项式乘回。普通行始终是非负指数多项式；来源向量可以为 Laurent 多项式。互素首单项式仅使用通常的 product criterion；它不改变源恒等式。

先寻求实际返回1；另预先固定两个目标及指数：
$$
(k+2)^n,\qquad(2\lambda-3)^n,\qquad n=1,2,3,4.
$$
对每一目标从1到4依次尝试，首次真实返回即停该目标。目标约化本身**不除其单项式或标量**。每次余式的完整身份为
$$
H^n-\operatorname{rem}(H^n)=\sum_{i=0}^{10}\Omega_i\,
\operatorname{in}(\widehat F_i).
$$
若余式真为零，还必须把每个初始归一乘子重新复合，完整返回原十一条未归一最低式上的同一 $H^n$；只有这一步完成才报成功。全部11来源坐标保留，实际为零的乘子也明确包含。

目标正幂的含义仅为该剩余初始理想上的严格幂零/支撑限制，供下一次 DVR blowup 使用。**不从模目标幂推出 QQ 原理想幂零、全 W 排空或有限整模型**。若目标未返回，只保其实际余式大小/SHA，不猜测是否存在解。单位1真返回才排除该估值 cell。

## 6. 首次执行边界

唯一新源：2026-11-28-unit211-W-b0-negative-e-full-I11-original-initial-two-positive-targets-8542.py。

源 SHA256：9f16b2f6490f948211850595d653166c20fbc4d452e5b5848c0cc26c99083187。
源大小：21072 B；零运行依赖。原定义和全一般低 D 来源以上述已刊源码/证明锁定，源本身自含。

预定180秒、4 GiB，外层建议195秒。不修改旧 b33，不重放旧七式/原投影/首项分区，不以第二素数或新点替换失败。输出只保存参数定义、所有实际阶段、次数、项数、字节数和 SHA；不保存可重算系数、原矩阵或数据分片。

首次执行之前，没有任何新单位、目标正幂、cell 排除或支撑中心被记为成功。原两目标全部零面、D 退化及所有未付首项均以实际返回为界保留。
