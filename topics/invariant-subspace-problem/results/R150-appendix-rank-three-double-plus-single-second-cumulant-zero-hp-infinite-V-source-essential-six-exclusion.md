# R150 附录：二重加单点 H 的零 Hp 层中 V 含无穷远源时无本质六维临界点

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：完整证明，两个冻结源码均已实际成功执行。** 在原完整临界系统的 rankH=3、H 型 2+1、rankV=2、Hp=0 层，若 V 的两个不同物理源之一为无穷远，则 ess(T3)≤5。证明覆盖整个有限孤立 H 源、所有降次源和两种异常源的全部剩余纤维。有限孤立 H 源且两个 V 源均有限的整支仍需继续。

## 1. 原输入、规范及所有射影边界

使用 [Hp0 九次 Gram 归约](R150-appendix-rank-three-double-plus-single-second-cumulant-zero-hp-nine-gram-candidates.md)。反设 ess(T3)=6，交换两个 V 列后，必可取
\[
H=z_0z_1^{\mathsf T}+z_1z_0^{\mathsf T}+\frac12w_{\rm vec}^2,
\quad V=\frac12(u^3+v^3),\quad F=h=g=1,
\]
\[
K_R=\begin{pmatrix}0&0&1\\0&b&-1/4\\1&-1/4&0\end{pmatrix},
\quad
b=-\frac{2e^3+1}{6}\ne0,\quad e=uKv\ne0,
\]
\[
z_0=\lambda u(s),\quad z_1=\mu u'(s)+\nu u(s),\quad
w_{\rm vec}=\rho u(w),\quad u=\sigma u(\infty),\quad v=\tau u(a),
\tag{1.1}
\]
λμρστ≠0。整个原六列 (y,z0,z1,wvec,u,v) 独立。

记 C0=K(z0,u)、C1=K(z1,u)、Cw=K(wvec,u)。v 的对应配对列准确等于 −C，且
\[
C_0^2=\frac1{4e},\quad
\frac{C_1}{C_0}=\frac{8e^3+1}{12},\quad
C_w^2=\frac{4e^3-1}{12e}\ne0.
\]
置
\[
Q=4e^3-1,\quad D=2e^3+1-12e^4,\quad
R=\frac{C_w}{C_0}=\frac DQ.
\]
已有 eQD≠0 和
\[
G_9(e)=16e^9-108e^8+36e^7-15e^6+18e^4-1=0.
\tag{1.2}
\]

原核为
\[
k(s,t)=-(t-s)^2q_s(t),\quad k(s,\infty)=-(s+1),
\]
\[
q_s(t)=s^3-5s^2+(s^3-3s^2+22s)t
-(3s^2+3s+5)t^2+(s+1)t^3,
\]
\[
b_s=K(u'(s),u'(s))=-2s^2(s-2)(s+6).
\tag{1.3}
\]
所有未写出的固定 K 约定与上述九次归约一致。

本分支的全部边界如下。a、w 有限，否则与 V 的无穷远列重合；s 有限，因为无穷远一阶 Taylor 列的 K 范数为零，与 b=μ²b_s≠0 矛盾。s∉{0,2,−6}；s,w,a 互不相同；s,w,a≠−1，分别由 C0、Cw、e 非零推出。还必须
\[
k(s,a)\ne0,\quad k(s,w)\ne0,\quad k(w,a)\ne0.
\tag{1.4}
\]
这些是原 C0、g、Cw 配对，均不假设其余普通点自动非零。

## 2. 两个精确三次几何式

相反 C0、C1 给
\[
(s+1)\partial_s k(s,a)-k(s,a)=0.
\]
定义
\[
\begin{split}
J_3(s,a)={}&5s(s+2)a^3-(11s^3+18s^2+8s+32)a^2\\
&+(4s^4-6s^3+34s^2+76s)a+4s^4-10s^3-20s^2.
\end{split}
\]
原核逐项身份为
\[
(s+1)\partial_s k(s,a)-k(s,a)=(a-s)J_3(s,a).
\tag{2.1}
\]
因 a≠s，故 J3=0。该式未除以 s+2；s=−2 时准确降为 32(3a+2)，仍包含在原系统中。

相反 Cw 又给
\[
E(s,a,w)=(s+1)k(w,a)-(w+1)k(s,a)=0.
\]
定义真实多项式
\[
C_3(s,a,w)=
\frac{E(s,a,w)-(w-s)(a-s)J_3(s,a)}{(w-s)^2}.
\tag{2.2}
\]
源码逐项验证分子整除，C3 关于 w 至多三次，领先系数准确为 −(s+1)(a+1)。在 J3=0、w≠s 下，原 E=0 等价于 C3=0。这里按多项式身份除去原已支付的 w−s，而非在一般点假定重根。

## 3. 两个来自完整 Gram 尺度的必要式

记 k=k(s,w)，
\[
d=\partial_s k/k,\quad
W=\frac1{s+1}-d,\quad q=\mu/\lambda.
\]
由原 c/g=−1/4 和 C1/C0=(8e³+1)/12，
\[
qW=-2b\ne0.
\]
又由 g=1、b=μ²b_s、Cw/C0=R，
\[
R\,W^2 k=4b b_s\frac{w+1}{s+1}.
\]
清除已支付分母，并用 (2.1) 将恰有的 (w−s)² 因子除去，得到
\[
\boxed{
F_1=3D\,J_3(s,w)^2
-2(2e^3+1)Q\,b_s(s+1)(w+1)q_s(w)=0.
}
\tag{3.1}
\]
源码同时验证它乘回 (w−s)² 正是原尺度式
\[
3D\{k-(s+1)\partial_s k\}^2
+2(2e^3+1)Q b_s(s+1)(w+1)k=0.
\]

从 e=στk(∞,a)、C0²=1/(4e)、g=1 及相反配对，第二式为
\[
\boxed{
F_2=D(a+1)k(s,w)+4e^2Q(w+1)k(s,a)=0.
}
\tag{3.2}
\]
因此每个原物理点必满足 J3=C3=F1=F2=G9=0。本证明用这些原必要式排空，不用已选均值或不完整极线替代原梯度。

## 4. 已实际执行的一般源消元

第一冻结源码准确计算
\[
R_i(s,a,e)=\operatorname{Res}_w(C_3,F_i),\qquad
N_i(s,e)=\operatorname{Res}_a(J_3,R_i).
\]
实际次数为
\[
\deg_sN_1=150,\quad \deg_sN_2=117,
\quad \deg_eN_1=54,\quad \deg_eN_2=45.
\]
任何有限共同根都使相应原结式为零，包括原领先项降次；因此不必为这些必要性除以 J3 或 C3 的领先项。

完整精确 QQ gcd 为
\[
G=80\,s^{18}(s+1)^{21}(s-2)^2(s+6)^2D_8(s)D_2(s)^2,
\tag{4.1}
\]
\[
D_2=15s^2+62s+32,
\]
\[
D_8=25s^8+410s^7+680s^6-10064s^5-8768s^4
+62976s^3+15488s^2-118016s+61440.
\]
deg_sG=55。源码乘回确认精确商 A=N1/G、B=N2/G，s 次数分别为 95、62；不存在未列出的 e 因子。

[无穷远孤立 H 源证明](R150-appendix-rank-three-double-plus-single-second-cumulant-zero-hp-infinity-essential-six-exclusion.md)已以模 37 Rabin 身份证明 G9 在 QQ 上不可约。故 Ke=QQ[e]/G9 是九次域。在 p=1031、e=700 时，A、B 的次数实际仍为 95、62，157 阶 Sylvester 行列式实际为
\[
\boxed{836\ne0.}
\tag{4.2}
\]
其条目在有限局部化整数环 Z[1/16,e]/(G9/16) 中；该环在此 e 值可映到 F1031。非零像证明原行列式在 Ke 中非零，因此是单位，在全部九个复嵌入下皆非零。这里没有从有限域空集直接推特征零空集。

所以除已支付的 s=0,−1,2,−6 外，所有源只可能满足 D8=0 或 D2=0。特别 s=−2 已被这个一般源门包含，并未因 J3 降次而漏掉。

## 5. 两个异常源的整个有限塔代数

第二冻结源码不重跑已经成功的嵌套结式。它从原核重建 J3、C3、F1、F2，并逐个核对第一源码已经输出的四个准确多项式 SHA-256；随后仅处理 (4.1) 的两条剩余异常源。

对 j=8,2，令 Aj=QQ[s]/Dj。源码确认 Dj 平方自由，并在整个 Aj 上准确求得
s(s+1)(s+2)(s−2)(s+6) 的逆。由此 J3 的领先项可在整个 Aj 上逆转，化为首一三次 a 式。

对该三次式，反复精确 gcd 和整除删除整个
\[
(a+1)k(s,a)=0
\]
主因子。这只删除原 (1.4) 和 a≠−1 已证明非物理的 a，不删除同一源的其他 a 纤维。全部 Euclid 首项逆均先在 QQ 上求出并乘回为 1，精确商也逐步乘回验证。两条源实际都恰删除一个一次主因子，各剩首一二次 Pj(a)。

现在保留整个三次 w 式 C3。在 Aj[a]/Pj 中，源码通过精确合成除法
\[
P_j(a)=(a+1)U_j(a)+P_j(-1)
\]
求得 a+1 的真实逆，且 Pj(−1) 的逆已在整个 Aj 上验证。因此 C3 的领先项 −(s+1)(a+1) 在整个 a 代数中可逆；将 C3 首一化得到有限自由塔
\[
B_j=A_j[a,w]/(P_j(a),\ \widehat C_3(s,a,w)).
\tag{5.1}
\]
这里保留每一个剩余 a 的全部三个有限 w 根，包括不必是物理点的其他根；没有除以 w−s、w+1 或任何 w 纤维函数去删根。

实际结构与乘法范数为：

| 整个异常源 | 剩余 a 次数 | 保留 w 次数 | QQ 维数 | F1 乘法行列式 mod 1031,e700 |
|---|---:|---:|---:|---:|
| D8=0 | 2 | 3 | 48 | 971 |
| D2=0 | 2 | 3 | 12 | 748 |

两个行列式均非零，实际选择 F1+λF2 的 λ 都为 0。源码对全部有限个有理分母验证模 1031 为单位，故这两个有限自由 QQ 代数延标至 Ke 后，F1 的乘法矩阵行列式在 Ke 中也非零，因而 F1 是单位。任一原点本来必须满足 F1=0，矛盾。

这一步不要求塔代数约化；有限自由模上的乘法矩阵可逆即可。32 个 QQ 逆的实际乘回记录，以及 a+1 和 C3 领先项的延拓逆乘回身份，支付了所有商环除法。

## 6. 源码和实际执行身份

第一源码 [2026-11-26-h21-zero-hp-finite-w-V-infinity-probe-347c.py](../notes/2026-11-26-h21-zero-hp-finite-w-V-infinity-probe-347c.py) 的 Git blob 为 72aadb75457c0a7fcfe87186694bebb1710cd67b，SHA-256 为 1c368de6e02f2c98ccfe076583828c98dcf90d235dcbfa468c3eb9326bebe207，冻结 commit 为 3d671b1c98f929848e2c437698cece6f8d2e033e。[run 45799548882 / job 139838879254](https://github.com/Rogerhu12/math-research-public/actions/runs/45799548882/job/139838879254) 实际 exit 0：源码计时 1.841419604 秒，驱动墙钟 2.218569082 秒，最大子进程 RSS 96680 KiB。该源码当时准确标为结构探针；其实际整数身份和行列式，在本文补完严格提升及全部异常纤维后才组成完整证明。

第二源码 [2026-11-26-h21-finite-w-V-infinity-exceptions-347c.py](../notes/2026-11-26-h21-finite-w-V-infinity-exceptions-347c.py) 的 Git blob 为 42fe7a5f4cf944deead5a76fc67760b0a929e758，SHA-256 为 f7c6c7b91c6de8efc266617014fd1e17d5a94bb18a80568b5ab8e69b9dc7707c，冻结 commit 为 c81ee4f55686ccce58b48538804ca3bf1e8da182。[run 45802044010 / job 139847488013](https://github.com/Rogerhu12/math-research-public/actions/runs/45802044010/job/139847488013) 实际 exit 0：源码计时 0.636825150 秒，驱动墙钟 0.943870784 秒，最大子进程 RSS 77140 KiB。

两次执行前均实际 pull main，并核对根及本课题 README Git blob 未变化；读过的真实提交分别即上述两个冻结提交。全部大多项式、QQ 逆和塔模数均由短源码重建，仅保留必要摘要与[真实小回执](../notes/2026-11-26-h21-finite-w-infinite-V-completed-execution-347c.json)。

## 7. 结论

一般源被 157 阶 Sylvester 单位排除，D8 与 D2 的全部尚可能 a、w 纤维又分别被 48、12 维原 F1 单位排除。故原本质六维反设不成立，整个所述 V 含无穷远源的 Hp0 层满足 ess(T3)≤5。

结合此前的孤立 H 源为无穷远排除，当前 H 型 2+1、Hp0 的潜在本质六维点只能有二重 H 源、孤立 H 源、两个 V 源全部有限。其原有限参数重建和剩余完整系数仍须解决。
