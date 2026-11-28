# R150：W/b0 内部 u 正估值的整个原 DVR 边界排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / r150_open_geometry。日期：2026-11-29（Asia/Taipei）。

**结论。** 当前正确 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 的原图，在剩余特征1009的赋值下不存在
$$
v(e)=v(k)=0,\qquad a=v(u)>0,\qquad u=e+1
\tag{1}
$$
的原解。证明保 mu 的零值、单位和任意极点，L/h/M 的全部首项下降以及任意分歧；没有把物理非零量自动当成赋值环单位。

先用同点原 $b_0,q_2,R_6,N_5$ 作完整纸面分层，把所有可能压到 $\bar k=2$ 的一个明确剩余图。唯一新执行在该图中返回两式 gcd 为1，并把正幂目标 $d^3$ 完整返到三个原剩余式；d 的非零性先由原 q2/R6 证明。因此这次排除的是整个 (1)，不是一个任取的有限域点。

这里处理的是内部原 DVR 边界，不是已闭的正 k 或 $u-1$ 图。其他内部已付分母的剩余零面、正 e 剩余图和整个 W 空性仍保留；本稿不从裸模空性提升任意 QQ 原纤维。

共同原定义：[完整 b0/N5 源](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob **47281af16fdd0ad7500ecda377c3cb9f9d65e725**、SHA-256 **e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8**。本文不重新执行该源、旧射线、初始理想、C74/C78、投影、PRS 或局部 jet。

## 1. 所有 k 剩余值共用的准确权缩放

置
$$
\ell=uL,\quad h=1-L,\quad m=uh,\quad
M=u^2 B,\quad B=L^2\delta-h^2,\quad Q=(u-1)k,
$$
$$
L=\frac{k^2+6k+4-2uk}{k(uk+2)},\quad
j=J/u=2(1-u)+LQ,\quad
\alpha=A_*/u=4Q-j,
$$
$$
C=C_*/u^3=\alpha h^2+j\delta L^2 .
\tag{2}
$$
$k$、$uk+2$ 均为赋值环单位，所以 L、h、B、j、alpha、C 全整。令 $q=\bar k\ne0$，则
$$
L_0=\frac{q^2+6q+4}{2q},\qquad
\alpha_0=\frac{q(q-2)}2,\qquad
j_0=-\frac{q(q+6)}2,\qquad
B_0=qL_0^2+2L_0-1.
\tag{3}
$$
$L_0=1$ 当且仅当 $q=-2$。$L_0=0$ 当且仅当 $q^2+6q+4=0$。

当 $\alpha$ 的剩余非零时，原 b0 精确给
$$
T=u\kappa\mu,\qquad \kappa=\frac{QL}{\alpha},\qquad
\mu=2\lambda-3,
$$
$$
A_2=(\mu^2+4\mu+5)/2,\quad
B_3=(\mu^3+6\mu^2+12\mu+7)/2 .
\tag{4}
$$
原 q2 归一为
$$
q_2/(2u^3)=CA_2-BLQ(3+2\mu)-4uQ\delta L\kappa^2\mu^2.
\tag{5}
$$
另有同点
$$
D=\ell A_2-T^2,\quad
K=\ell^2B_3-3\ell A_2T+2T^3,\quad
MK^2-4m^2D^3=0,
$$
$$
D=MS,\qquad
S=\frac{A_*A_2-\ell Q(3-4\lambda)}{4uQ\delta\ell}.
\tag{6}
$$
(6) 的 S 只在下文明证其分母剩余非零或其准确阶数时使用。不把物理单位自动当成赋值环单位。

## 2. q 不等于二：一般 L/h 支及任意深 M

先设 $L_0h_0\ne0$、$q\ne2$，因此 alpha 为单位。

若 mu 有极点，$D/(u\mu^2)\to L_0/2\ne0$，
$v(K)\ge2a+3v(\mu)$，$v(M)\ge2a$。原 R6 两项估值分别至少
$6a+6v(\mu)$、准确 $5a+6v(\mu)$，不可能相消。故 mu 整。

此时 R6 除 $u^5$ 强迫 $\bar A_2=0$，原 (5) 再迫 $B_0=0$：
因为 L、Q 非零，而 $3+2\bar\mu=0$ 与 $A_2=0$ 不相容。特别 lambda、$3-4\lambda$ 和 $B_3=-\lambda$ 的剩余都非零。

现在允许 B 的任意深相消。令 $b=v(B)>0$，则 $\delta$ 必为单位，否则 $B_0=-h_0^2\ne0$。且 $q\ne-4$，因为 q=-4 时 $L_0=1/2,B_0=-1$；所以 $\Phi\to-(q+4)$ 也是单位。由 (6)，S 的分子首项来自 $-\ell Q(3-4\lambda)$，得
$$
v(D)=a+b,\qquad v(K)=2a.
$$
R6 两项估值 $6a+b$、$5a+3b$ 迫
$$
b=a/2.
\tag{7}
$$

完整 N5 在这里给严格矛盾。记
$$
t=\overline{T_0/u}=2+qL_0,\quad
p=\overline{P_{02}/u}=4+q+2qL_0,\quad
g=\overline{G/u}=\bar\lambda p-t.
$$
原 $B_0=0$ 给 $t^2=p$；t=0 会使 $B_0=L_0(qL_0+2)-1=-1$，故 p 非零。原
$$
y_s=(\ell T_0/2-uV_s)/M
$$
的分子除 $u^2$ 的剩余是
$$
Y=L_0t/2+g/(-q)=p(1/2-\bar\lambda)/q\ne0.
$$
最后非零性用 $A_2=0$，并非新增头假设。于是
$$
v(y_s)=-b,\quad v(z_2)=a-b,\quad
v(z_1)\ge a-b,\quad v(Z_0)\ge3a.
$$
在完整
$$
N_5=2mD(Z_0+Dz_2)+MKz_1
\tag{8}
$$
中，$2mD^2z_2$ 的阶是 $4a+b=9a/2$，而另外两项阶至少 $5a$。其非零首项不能相消。一般支包括全部深 M 因而排除；q=-1 的 delta 深分支已经在一般 R/q 步排除，不曾倒 delta 的零首项。

## 3. L0 等于零与 q 等于负二

### 3.1 L0=0

此时 $q^2+6q+4=0$，$\alpha_0,h_0,\delta_0,\Phi_0$ 都非零，$B_0=-1$。令 $b=v(L)>0$。

原 (5) 先排 mu 极点，再给 $A_2=0$ 的剩余及
$$
A_2/L\longrightarrow\frac{q(3+2\bar\mu)}{\alpha_0}\ne0.
$$
因此
$$
v(D)=a+2b,\qquad v(K)=2a+2b.
$$
R6 迫 $b=a/2$。

完整原恢复给
$$
g=\bar\lambda(q+4)-2\ne0,\qquad z_2/u\to2g/(-q).
$$
若 g=0，$A_2(2/(q+4))=0$ 与 $q^2+6q+4=0$ 相减迫 q=2，而后式在 q=2 为20，矛盾。因此 N5 中 $2mD^2z_2$ 的阶准确 $6a$；$2mDZ_0$ 与 $MKz_1$ 的阶至少 $7a$、$13a/2$。此支全排。

### 3.2 q=-2

此时 $L_0=1,B_0=-1,\alpha_0=4$；令 $c=v(h)>0$，允许任意深 m。原 q2 排 mu 极点，有限剩余必须满足
$$
\bar\mu^2+2\bar\mu+2=0.
$$
据此
$$
D/u\to A_2=\bar\mu+3/2\ne0,\quad
K/u^2\to(7\bar\mu+10)/4\ne0,\quad
z_2/u\to2\bar\lambda\ne0 .
$$
上述两可能零值代入该二次分别给 $5/4$、$58/49$，非零；lambda=0 亦不满足该二次。R6 两项的阶 $6a$、$5a+2c$ 迫 $c=a/2$。原恢复有 $v(z_1)\ge a,v(Z_0)\ge3a$，所以 N5 的 $2mD^2z_2$ 阶 $4a+c=9a/2$，余项至少 $5a$，再次矛盾。

因此到此只保 q=2。没有 q=0 情形，因为 k 在 (1) 是单位。

## 4. q=2 的全部 alpha/mu 相对阶

现在
$$
L_0=5,\quad h_0=-4,\quad B_0=59,\quad
Q_0=-2,\quad\delta_0=3,\quad\Phi_0=-6.
$$
设 $\gamma=v(\alpha)>0$。原 W/b0 图已经付清 $A_*\ne0$，故 $\alpha\ne0$；以下使用其准确正阶，不假定其首值为单位。mu 等于零的可能性由下述完整 q2 常数项排除，不提前把它当单位。
$$
v(T)=a-\gamma+v(\mu).
$$
令 $X=T^2/u$。q2 的完整最低缩放为
$$
q_0=12X-30\mu^2-2\mu+27
\tag{9}
$$
（准确是 $q_2/(20u^3)$ 的所列剩余）。

若 $\gamma<a/2$，q2 先排 mu 极点，并迫 mu 为单位、$30\mu^2+2\mu-27=0$；$A_2$ 非零。此时
$v(D)=a,\ v(K)=2a-\gamma$，R6 两项 $6a-2\gamma$、$5a$ 严格不同，故全排。

若 $\gamma>a/2$，q2 迫 $v(\mu)=\gamma-a/2>0$、
$\bar X=-9/4$。从而
$$
D/u\to59/4,\qquad K/(uT)\to-42.
$$
R6 除 $u^5$ 的剩余为
$$
-59\cdot7450\ne0\pmod {1009}.
$$
此支全排。

只余 $\gamma=a/2$。若 mu 有极点，q2 迫
$X/\mu^2\to5/2$，因而 $v(D)>a+2v(\mu)$，但
$K/(uT\mu^2)\to-5/2$，R6 第一项严格较低，矛盾。若 mu 为正估值，(9) 剩27。故唯一未闭图是
$$
\gamma=a/2,\qquad v(\mu)=0,\qquad X\in\kappa^\times .
\tag{10}
$$

## 5. 剩余中心的同点 q2/R6/完整 N5 三式

从此只在同一剩余域记 mu、X。令
$$
A_2=(\mu^2+4\mu+5)/2,\quad d_{\rm raw}=5A_2-X,\quad
H_{\rm raw}=-15A_2+2X,
$$
$$
g=13\mu+27,\qquad
Y=\frac{33-13\mu}{118},\qquad z=g+16Y .
$$
直接完整原恢复给
$$
V_s/u\to g/2,\quad
t_s u/T\to52/59,\quad y_s\to Y,
$$
$$
z_1/T\to-4Y,\quad z_2/u\to z,\quad Z_0/u^2\to gX .
\tag{11}
$$
最后一式使用完整 Z0；没有把物理 f 设成零。

因此三个同点原剩余式是
$$
q_0=12X-30\mu^2-2\mu+27,
$$
$$
R_0=59XH_{\rm raw}^2-64d_{\rm raw}^3,
$$
$$
N_0=-8d_{\rm raw}(gX+d_{\rm raw}z)-236XH_{\rm raw}Y.
\tag{12}
$$
其准确原尺度为 $q_2/(20u^3)$、$R_6/u^5$、$N_5/u^4$，不是三个无来源的独立范数。

若 $d_{\rm raw}=0$，由 $X\ne0$ 得 $H_{\rm raw}=-X$，R0 为 $59X^3\ne0$。因此原式已证明 $d_{\rm raw}\ne0$。由 q0 再得
$$
n=2\mu+3\ne0,\qquad d=59n/12=d_{\rm raw},\qquad r=X/d .
$$
这是对一个已证明非零的剩余数作换元，不倒物理 D 或未知首项。

定义
$$
q=15n^2-(88+118r)n+75,\qquad
R=59r(r+3)^2-64,
$$
$$
H=59r^2+413r+204,\qquad
N=(105-13n)H-28320(r+1).
\tag{13}
$$
其中 $q_0=-q/2$，而 (12) 在 (13) 的任意 n,r 多项式环中仍完整有
$$
R_0=d^3R+qE_R,\qquad
N_0=d^2N/59+qE_N.
\tag{14}
$$
源码显示并逐项返回
$$
E_R=\tfrac{59}4X(X+3d)+\tfrac{59}{64}Xq
      -8d^2-\tfrac13dq-\tfrac1{216}q^2,
$$
$$
E_N=-gX/3-2dz/3-qz/72+(59/2)XY.
$$
这里 $X=dr$，$d_{\rm raw}=d+q/24$；所以 (14) 未先令 q=0 丢掉原来源。

## 6. 固定消元及最后三个原式的正幂返回

在 $\mathbb F_{1009}[r]$ 中写
$$
N=a(r)n+b(r),\quad a=-13H,\quad b=105H-28320(r+1),
$$
$$
q=15n^2+B(r)n+75,\qquad B=-88-118r.
$$
固定一次式/二次式消元为
$$
E=15b^2-Bab+75a^2
=a^2q-(15an+Ba-15b)N .
\tag{15}
$$
不反演 H 或 a，全部首项下降都在这条整式身份内保留。

只作预定的一个真实 Bézout
$$
s_RR+s_EE=g(r),
$$
其中 g 首一。把 (15) 代回得
$g=\Omega_q q+\Omega_RR+\Omega_NN$；再用 (14) 得
$$
d^3g=
\{-2[d^3\Omega_q-\Omega_RE_R-59d\Omega_NE_N]\}q_0
+\Omega_RR_0+59d\Omega_NN_0.
\tag{16}
$$
源码返回 (16) 的全部普通二元坐标，没有用裸模 rank、只一根、D 模幂零或无来源饱和判断。

本次唯一实际返回 $g=1$，并核完 (16) 的全部普通二元坐标。因此若三个完整原剩余式同时为零，(16) 就迫 $d^3=0$；但 §5 已经从原 q2/R6 证明 d 非零。这个矛盾排除了 (10) 的整个剩余图。没有选择 n 或 r 的一个有利根，也没有删除消元一次式的头 a=0。

## 7. 实际执行与小回执

[新源](../notes/2026-11-29-unit211-W-b0-internal-u-positive-k-two-three-original-residues-8542.py)零依赖，预定 **30 秒 / 256 MiB**，固定 p=1009。源 blob **567c6e6be3d33fe470b274413a216cc16952f0b4**，6254B，SHA-256 **85f7ccc8950aafd0634c1de9aec2522d37530af9682a8162ba25215c06046e75**。

[正式首次输入](../notes/2026-11-29-unit211-W-b0-internal-u-positive-k-two-three-original-residues-8542-input.md) blob **389b477edbe6293dfdfbf23b4245eecdab9bc8ed**，8979B，SHA-256 **8712854ee5e6da9d40baae86533b9b416edaa5e160d23881e7436666fa7e0c36**。其 §4 已准确写为由原已付 $A_*\ne0$ 证明 alpha 非零；mu=0 保留到原 q2 常数项排除。该首次前文字修正没有改动源码或数学预算。

唯一 [run 46176850224](https://github.com/Rogerhu12/math-research-public/actions/runs/46176850224)，job **141077389285**。两个数学记录均已亲读：

- 原 R 的次数3、新 E 的次数5，完整 gcd 次数0且规范值为1；最后三原式目标确为 $d^3$。
- 5 条完整缩放身份、3 条三源组合、5 次商余乘回、22 次域逆乘回；没有追加另一组、换 p 或重做旧原投影。
- 实际 **0.02559295400000039 秒 / 38292 KiB / exit 0**；最后数学阶段 **0.0014591990000027977 秒**。
- source commit **4c463f2f670730345fa93a36ba726cb189bbf707**；实际 pull 到 **0212de454a8c91a07c54f052e71d19a205f6a1d6**，**2026-11-28 18:37:30.520631 UTC**，两 README 与已读版本相同。
- stdout **2412 B**，SHA-256 **2f4b5ef9a50cb0d0a4f9004168bd7fdf881b610b32746b286a73224df83d12c8**。

完整三原目标的规范 profile 是 n 次数3、r 次数0、单项；SHA-256 **39052f4d9eca3af0ba463e8784ff75833c87193050945d7bb9bad3c40302bfb4**。三个实际乘子全部回乘，未以裸 gcd 替代原式必要性。

[小回执](../notes/2026-11-29-unit211-W-b0-internal-u-positive-k-two-three-original-residues-receipt-8542.json)保存完整两个原始数学记录、实际执行状态及来源身份；不存大系数、jet 或编码缓存。

## 8. 全部分支的闭合及保留范围

(3) 使 k 的所有非零剩余值分成四类：一般 $L_0h_0\ne0,q\ne2$；$L_0=0$；q=-2；q=2。§2 保一般类的任意深 M，§3 处理整 L 零及任意深 m，§4 完整分开 q=2 的三种相对阶及全部 mu 阶。只有 (10) 需要新执行，现由 §6 的原 $d^3$ 身份关闭。因此不存在 (1) 的原解。

本稿没有将原 D 的幂零模证书提升成 QQ 结论，也没有把某个普通容器当成自由商。实际有限域运算只用于一个已由完整原赋值缩放推出的必要剩余系统；原剩余 d 是单位，所以正幂返回立即给矛盾。原物理图、全部原值同点要求和未处理的内部已付分母边界均保持原范围。
