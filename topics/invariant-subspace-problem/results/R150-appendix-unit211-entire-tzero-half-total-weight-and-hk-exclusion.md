# R150 补充：整个原 t=0 的半总权与 h=k 值碰撞排除

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 1. 新结论与原范围

保持原 unit211 非零孤立 mean 的完整均值、N/P 值和 jet 条件，
原最高基值 $P_{02}\ne0$、$\lambda\ne0$，以及原物理列的非退化配对。
本篇证明：

1. 整个原 $t=0$ 层都满足 $\ell=b+c=1/2$；
2. 在值碰撞 $h=k$ 上，$t=0$ 强迫
   $\lambda=1/2,\ h=k=w=0$；
3. 该唯一原值形状由已经完成的完整五列 Gram 物理秩排除，
   因而当前整个 $h=k$ 值碰撞图可以支付 $t\ne0$。

前两步不使用 $\Phi$、W、$P_f$ 或 $D$ 的逆，第三步不借用任何
$D\ne0$ 图的排除。尤其 $h=k$ 本来就在值判别式零面；
不能把此前 W 或 Phi 的 $t=0$ 排除搬到这里。

## 2. 七个自由原参数的真正 mean 身份

取 $b,c,p,q,X,Y,\eta$ 自由，令
$$
\ell=b+c,\quad a=1-\ell,\quad u=bp+cq,\quad
f=u+\eta,\quad V=bX+cY.
$$
在整个 $t=0$ 上置
$$
r=X-ap,\quad s_G=Y-aq,\quad A_1=2f-2V,
$$
并构造同一原 Gram 四行
$$
g_0=(0,0,p,q),\quad g_1=(0,A_1,r,s_G),\quad
g_B=(p,r,0,0),\quad g_C=(q,s_G,0,0).
$$
乘法与迹始终为
$$
(vz)_1=v_0z_1+v_1z_0,\qquad
\tau(v)=av_0+v_1+bv_B+cv_C.
$$
记 $d=DK(\mathbf1)=(u,d_1,X,Y)$，其中
$$
d_1=2f-V-au,\qquad F_2=\tau(d)=2f.
$$
所有原均值使用 $-2(d^2)_j$；第一 jet 的平方项确为 $-4ud_1$。

设
$$
E_W=bE_B+cE_C,\qquad
V_2=bp^2+cq^2,\quad W_1=bpX+cqY.
$$
直接由原均值得到
$$
E_0=V_2-2W_1-2u^2+4fu.
$$
将同一个 $d,DK(d)$ 代入另外三条原均值，精确有
$$
\boxed{
E_1-E_W+(1-\ell)E_0=4(f-u)A_1.
}
\tag{1}
$$
等价地，左端也等于 $-8(f-u)(V-f)$。
这是整个七变量整数多项式环的身份，未先施加 $E_0=0$，
未倒 $f-u$、$V-f$ 或 $u$。

本次独立小源只检查新的 (1) 与下文两个小原值身份。
它没有重跑自由 $f,t$ 的完整 N/P 门、任何旧结果式或几何排空门。

所有原均值为零时，(1) 立即给
$$
\boxed{\eta A_1=0.}
\tag{2}
$$
可以保留这一个乘积，不必分别倒置两个因子。

## 3. 完整 N/P 身份迫半总权

沿用已经完成的
[自由 f、t 完整原低 weighted N/P 恒等式](R150-appendix-unit211-unrestricted-f-and-t-original-low-weighted-NP-identities.md)。
在所有原条件下，那里两式为
$$
2P_{02}(2\lambda-1)w=bc\,t\,\widehat K_w,
$$
$$
2P_{02}\lambda(2\ell-1)
=4u\eta A_1+bc\,t\,\widehat K_\lambda.
$$
它们包括 $t=0$，没有将自由 $\eta$ 项删掉。

现在只用 $t=0$ 和 (2)。因 $P_{02}\lambda\ne0$，得到
$$
\boxed{\ell=\frac12,\qquad (2\lambda-1)w=0.}
\tag{3}
$$
这里不需要 $u\ne0$，也没有把 $w$ 或 $2\lambda-1$ 作单位。
(3) 是整个当前原 $t=0$ 层的必要条件，尚不单独排空一般
$h\ne k$ 的值图。

## 4. h=k 上的全部值碰撞只余 lambda=1/2

记共同单点值为 $h$，原值向量为 $(1,w,h,h)$。
三个真正原矩是
$$
a+w+\ell h=\lambda,\qquad
a+2w+\ell h^2=2\lambda^2,\qquad
a+3w+\ell h^3=4\lambda^3.
$$
使用 (3)，定义其两倍误差
$$
m_1=1+2w+h-2\lambda,\qquad
m_2=1+4w+h^2-4\lambda^2,
$$
$$
m_3=1+6w+h^3-8\lambda^3.
$$
原点均有 $m_1=m_2=m_3=0$。令 $\kappa=2\lambda-1$，
以免与第二单点值 $k$ 混用。完整小多项式身份为
$$
\boxed{
m_2-(h+2\lambda-1)m_1
=-2\kappa+2(3-h-2\lambda)w.
}
\tag{4}
$$
于是原点满足
$$
\kappa=(3-h-2\lambda)w.
$$
由 (3) 的 $\kappa w=0$，乘以 $\kappa$ 得 $\kappa^2=0$。
在原复数点上即 $\kappa=0$，故 $\lambda=1/2$。
这一步保留全部因子零面，没有先在 $\kappa\ne0$ 上取商。

此时
$$
m_1=h+2w,\quad m_2=h^2+4w,\quad m_3=h^3+6w,
$$
并且完整有
$$
\boxed{m_3-(h+2)m_2+(2h+1)m_1=h.}
\tag{5}
$$
故 $h=0$，再由 $m_1=0$ 得 $w=0$。没有漏掉三次矩，
也没有把一个单点的值用于另一个原点。

## 5. 必须使用原第五列的物理排除

所得形状是
$$
\lambda=\frac12,\quad a=\ell=\frac12,\quad h=k=w=0.
$$
它自动属于 $S=h+k+1-2\lambda=0$，因此准确落入独立的
[347c 全 lambda=1/2 原物理排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-equal-values-lambda-half-exclusion.md)。

该已刊证明的 $t=0$ 部分保留原孤立点第五列：原 $N(V)$ 先给
$A_1=0$，原 $E_0,N_0$ 与非零 $P_0$ 再给
$r=s_G=0,\ f=u/2$。在其 $p=1$ 的合法原尺度中，五列 Gram 是
$$
G_{\mathrm{phys}}=
\begin{pmatrix}
0&0&1&q&U_0\\
0&0&0&0&0\\
1&0&0&0&0\\
q&0&0&0&0\\
U_0&0&0&0&0
\end{pmatrix},
\qquad U_0\ne0.
$$
它的秩为 $2$。同一原长度五除子在非退化六维物理空间中给五个
线性无关值/jet 列；其张成空间的根空间维数至多 $1$，
所以限制 Gram 的秩至少 $4$。矛盾。

本篇完整核对了该已刊证明的适用范围；没有重跑其小源，
没有把四列活跃 Gram 秩二单独用作矛盾，也不把这个物理排除
误记成尚未构造的纯抽象均值单位理想。

## 6. 首次精确返回与后继范围

[新小源](../notes/2026-11-28-unit211-entire-tzero-mean-and-hk-value-identities-8542.js)
3813 字节，SHA256
614240007765bc41732006cf2b792e888566428267ac0a8ebad37d5399047980。

- 首次纯 V8 BigInt 实际 1 ms、170 次整数多项式乘法；
- (1)、(4)、(5) 三个完整多项式差式全零；
- 原七自由参数与后两个独立形式值参数的作用范围分开声明；
- 没有使用数值近似、旧错误 compact 或已冻投影门。

[小回执](../notes/2026-11-28-unit211-entire-tzero-mean-and-hk-value-identities-execution-8542.json)
保留实际身份。另一位代理独立静态复核了 (2)–(5) 的逻辑和所有除法范围。

因此当前整个 $h=k$ 物理值碰撞可用 $t\ne0$；
若采用 $z=Qt$ 且当前图原 $Q\ne0$，亦可用 $z\ne0$。
其余 $t\ne0$ 原图、未付权面、完整 R150 和普通 Hilbert ISP 仍须继续。
