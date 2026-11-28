# R150 补充：W/b0 正 e、k 剩余值负二时整个 ell 极点的原式排除

日期：2026-11-29（Asia/Taipei）；会话 Astra-ISP-8542378f-20261127。

## 1. 结论、范围与原来源

在当前 W/b0 原图的剩余特征 $1009$ 赋值分析中，若
$$
v(e)=a>0,\qquad v(k)=0,\qquad \bar k=-2,
$$
则不可能有 $v(\ell)<0$。本结论覆盖任意正有理相对阶、$\mu=2\lambda-3$ 的全部阶、$M$ 的任意深首项相消以及全部原 $D$ 首项退化；不倒 $D$ 或任何新首项。

这是当前赋值边界的原式结论，不是把有限域计算直接提升成任意 QQ 纤维空性。五条其他无穷射线已经分别关闭；整个正 e 射线、内部权图和有限 DVR 模型仍须各自完成，普通 ISP 尚未完成。

已刊来源：

- [正 e 的原 lambda 限制](R150-appendix-unit211-W-b0-positive-e-ray-original-lambda-valuation-and-two-pole-centers.md)；
- [k 剩余值负二时正 ell 排除和 Z 整性](R150-appendix-unit211-W-b0-positive-e-k-minus-two-positive-ell-exclusion-and-integral-center.md)；
- 原完整 q2/R6/N5 定义源 blob **47281af16fdd0ad7500ecda377c3cb9f9d65e725**，SHA-256 **e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8**。

该原定义源不在本次重新执行。新执行只针对下文 §6 的两个新剩余原式。

## 2. 全部情况共用的原恒等式

设 $b=-v(\ell)>0$，并定义
$$
\beta=\frac u\ell,\qquad
B=\frac M{\ell^2}=\delta-(\beta-1)^2=-Q+2\beta-\beta^2,
$$
$$
g=4\beta-1+\frac{2\beta}{k},\qquad
\mathcal C=\frac{C_*}{\ell^3Q}
 =B\left(1-\frac{2\beta}{k}\right)+4\beta(\beta-1)^2.
\tag{1}
$$
这里 $u,\delta\to1$、$Q/e\to-2$、$v(\beta)=b$、$\bar g=-1$。原 b0 关系准确给出
$$
T=\frac{u\mu}{g},\qquad
A_2=\frac{\mu^2+4\mu+5}{2},\qquad
B_3=\frac{\mu^3+6\mu^2+12\mu+7}{2}.
\tag{2}
$$
原 q2 除以 $\ell^3Q$ 为
$$
\mathcal C(\mu^2+4\mu+5)-2B(3+2\mu)
       -\frac{8u\delta\beta^2\mu^2}{g^2}=0.
\tag{3}
$$
没有在 (3) 中倒 $M$。另两条完整必要关系是
$$
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell A_2T+2T^3,
$$
$$
R_6=MK^2-4m^2D^3=0,\qquad
N_5=2mD(Z_0+Dz_2)+MKz_1=0.
\tag{4}
$$
由原 q2 可用完整恒等式
$$
D=MS,\qquad
S=\frac{A_*A_2-\ell Q(3-4\lambda)}
        {4uQ\delta\ell}.
\tag{5}
$$
此式在 $M$ 任意高阶相消时仍保留。

## 3. b 小于 a

这时 $B/\beta\to2$、$\mathcal C/\beta\to6$。若 $\mu$ 有极点，(3) 的二次最高项唯一最低阶，故不可能。于是 $\mu$ 整，而且
$$
3\bar\mu^2+8\bar\mu+9=0.
\tag{6}
$$
同时 $T$ 整，
$$
M/\ell\to2,\quad m/\ell\to-1,\quad
D/\ell\to A_2,\quad K/\ell^2\to B_3.
$$
这些剩余式允许 $A_2$ 或 $B_3$ 为零，不另取新头开集。
由 $R_6/\ell^5$ 得
$$
2B_3^2-4A_2^3=0.
$$
令 $n=\bar\mu+2$，则 (6) 和这个完整剩余关系分别成为
$$
3n^2-4n+5=0,\qquad
-\frac12n^2(3n^2+2n+3)=0.
$$
第一式排除 $n=0$。两个二次相减给 $6n-2=0$，即 $n=1/3$，但第一式此时等于 $4\ne0$。故整个 $b<a$ 排除。

## 4. b 大于 a

此时 $B/(-Q)\to1$、$v(B)=a$、$\mathcal C/B\to1$。先用 (3) 排 $\mu$ 极点，再取剩余得 $\bar\mu=\pm1$。

若 $\bar\mu=1$，则
$$
D/\ell\to5,\qquad K/\ell^2\to13.
$$
$MK^2$ 与 $4m^2D^3$ 的阶分别为 $a-6b$、$-5b$，前者严格较小，不能相消。

若 $\bar\mu=-1$，写 $\epsilon=\mu+1$。从 (1)、(3) 的完整展开得到
$$
\frac{\epsilon}{\beta/B}\to4,\qquad
\frac{B_3}{\beta/B}\to6.
\tag{7}
$$
具体地 $\mathcal C/B-1\sim4\beta/B$，(3) 首项为
$-2\epsilon+8\beta/B$；其余项阶严格更高。于是
$$
T\to1,\qquad D/\ell\to1,\qquad
K/(\ell/B)\to6.
$$
这里第二个 K 项除以 $\ell/B$ 后含 $B$，故不会改变最后一个非零剩余。现在 R6 两项的阶分别为
$$
-4b-a,\qquad -5b.
$$
因 $b>a$，这次是后者严格较小，仍不能相消。整个 $b>a$ 排除。

## 5. b 等于 a：先排极点和深 M 中心

令
$$
r_0=\overline{\beta/e}\ne0.
$$
有
$$
B/\beta\longrightarrow2+\frac2{r_0},
\qquad
M/\ell\longrightarrow2+\frac2{r_0}.
\tag{8}
$$
此处允许 $r_0=-1$，因此 (8) 的剩余可以为零。

若 $\mu$ 有极点，则
$$
\frac D{\ell\mu^2}\to\frac12,\qquad
\frac K{\ell^2\mu^3}\to\frac12,\qquad
m/\ell\to-1.
$$
原 $R_6/(\ell^5\mu^6)$ 的剩余为
$$
\frac14\left(2+\frac2{r_0}\right)-\frac12
       =\frac1{2r_0}\ne0.
$$
故 $\mu,\lambda,T$ 全部整。以下字母 $\mu,\lambda,A_2,B_3$ 均表示相应剩余值。原 (3) 除以 $2e$ 给出
$$
r_0 f_0+\mu^2-1=0,\qquad
f_0=3\mu^2+8\mu+9.
\tag{9}
$$

若 $r_0=-1$，(9) 给 $A_2=0$。此时 $\lambda\ne0$ 且
$B_3=-\lambda\ne0$。令 $w_B=v(B)>a$。有
$$
\ell e\to-1,\quad \ell Q\to2,\quad A_*\to-2.
$$
(5) 的分子第一项有正阶，第二项剩余为
$-2(3-4\lambda)\ne0$；因为 $3-4\lambda=0$ 会使
$A_2=5/8\ne0$。分母剩余为 $8$，所以 $S$ 为单位，$v(D)=v(M)=w_B-2a$。
又 $K/\ell^2\to B_3\ne0$、$v(m)=-a$，故 R6 两项的阶为
$$
w_B-6a,\qquad 3w_B-8a.
$$
其差的绝对值为 $2(w_B-a)>0$。这排除了整个深 M 中心，包括任意更深的相消；没有只检查第一个非零导数。

## 6. b 等于 a 且 r0 不等于负一：完整 N5 和两个新剩余原式

由 (9)，$f_0=0$ 会推出 $\mu^2=1$，但
$f_0(1)=20$、$f_0(-1)=4$，矛盾。因此
$$
n_0=1-\mu^2=r_0f_0\ne0,\qquad
r_0=\frac{n_0}{f_0},\qquad
r_0+1=\frac{4A_2}{f_0}\ne0.
\tag{10}
$$
特别 $A_2$ 也非零。下文所有这些逆均由 (9)、当前分支和
$r_0\ne0$ 证明，不是新增的物理假设。

完整原恢复的常数系数逐项给出
$$
T\to-\mu,\quad w\to\frac{3\mu+1}{2},\quad
\frac M\ell\to\frac{2(r_0+1)}{r_0},\quad
\frac m\ell\to-1,
$$
$$
T_0,\Phi\to\frac2{r_0},\quad P_{02}\to-\frac2{r_0},
\quad G\to-\frac{2\lambda}{r_0},
\quad P_c\to\frac{4(1+\lambda)}{r_0^2},
$$
$$
\frac{V_s}{\ell}\to1,\quad
t_s\to\frac{2r_0(1+\lambda)}{r_0+1},\quad
y_s\to\frac{1-r_0}{2(r_0+1)}.
\tag{11}
$$
例如 $V_s=-G/Q-P_c/(Q\Phi)$ 的两项除以 $\ell$ 后依次趋于
$-\lambda$、$1+\lambda$，其和确为 $1$。这里 $s$ 标记原 f 常数系数；没有令物理 f 等于零。

将 (11) 代入完整原 $Z_0,z_1,z_2$，得到
$$
Z_{00}:=\lim Z_0/\ell^2=-\mu(\mu+1),
$$
$$
z_{20}:=\lim z_2/\ell=\frac4{r_0+1}-\mu-5,
$$
$$
z_{10}:=\lim z_1/\ell
=\frac{r_0\mu^2+r_0\mu-2\mu-r_0-1}{r_0+1}.
\tag{12}
$$
所以在同一点、同一个 $\mu$ 上，原 R6 和完整 N5 必须同时给出
$$
R_{\rm lead}:=\frac{2(r_0+1)}{r_0}B_3^2-4A_2^3=0,
$$
$$
N_{\rm lead}:=-2A_2(Z_{00}+A_2z_{20})
              +\frac{2(r_0+1)}{r_0}B_3z_{10}=0.
\tag{13}
$$
其准确缩放为 $R_6/\ell^5$ 和 $N_5/\ell^4$。这没有把两个独立范数的根事后配成同一点。

定义新的两个一元多项式
$$
F_R=2B_3^2-n_0A_2^2,
$$
$$
H_\mu=\mu^4+7\mu^3+17\mu^2+25\mu+10,
$$
$$
F_N=n_0A_2(\mu+1)(\mu^2+4\mu+7)-2B_3H_\mu.
\tag{14}
$$
代入 (10) 后完整有理原身份为
$$
\frac{r_0}{2}R_{\rm lead}=\frac{2A_2}{f_0}F_R,
\qquad n_0N_{\rm lead}=F_N.
\tag{15}
$$
它们与 (11)、(12) 的两个中间完整身份在唯一新执行中全部返回。因此 (13) 强制 $F_R=F_N=0$。

在 $\mathbb F_{1009}[\mu]$ 中，本次返回以下可直接复核的完整 Bézout 身份：
$$
A(\mu)F_R+B(\mu)F_N=(\mu+1)^2,
\tag{16}
$$
其中
$$
A=116+682\mu+173\mu^2+589\mu^3
       +732\mu^4+13\mu^5+263\mu^6,
$$
$$
B=540+503\mu+206\mu^2+491\mu^3+884\mu^4+636\mu^5.
$$
对应的两个原式为
$$
F_R=775+74\mu+366\mu^2+87\mu^3+793\mu^4+8\mu^5+253\mu^6,
$$
$$
F_N=452+251\mu+46\mu^2+68\mu^3+253\mu^4
       +416\mu^5+487\mu^6+503\mu^7.
$$
(10) 已经证明 $\mu+1\ne0$，故 (16) 与同点原式同时为零矛盾。全部 $b=a$ 排除。

## 7. 唯一实际执行和不扩张的结论

新源：

[2026-11-28-unit211-W-positive-e-k-minus-two-ell-pole-original-residue-bezout-8542.py](../notes/2026-11-28-unit211-W-positive-e-k-minus-two-ell-pole-original-residue-bezout-8542.py)

新输入：

[2026-11-28-unit211-W-positive-e-k-minus-two-ell-pole-original-residue-bezout-8542-input.md](../notes/2026-11-28-unit211-W-positive-e-k-minus-two-ell-pole-original-residue-bezout-8542-input.md)

源 blob **3f9e586d76911d47f0530239480a56bc07d79c42**；
SHA-256 **7a09280436c64f609c275c24b0574d0741956557066081902b07844f72a47f52**。
唯一 [run 46171289266](https://github.com/Rogerhu12/math-research-public/actions/runs/46171289266)，job **141060069093**：

- 预定 30 秒、256 MiB，外层 45 秒；实际 **0.030981101000008948 秒 / 38012 KiB / exit 0**；
- 四个完整有理原身份、531 次精确除法、153 个含有理规范化的 Bézout 返回；不能将后两者误称 531 或 153 个不同数学门；
- 最后数学阶段 **0.007347121000009338 秒**，实际 gcd 为 1，完整已付目标为 $(\mu+1)^2$；
- stdout **1826 B**，SHA-256 **171e7f6743ea4a2185be48a405b17bf7801fecb22c4acb82ac8c5fff81472d11**；
- 实际 pull/rebase 到 **8c4936f3ea7c1fd8caaee057fce69b783dd05475**，**2026-11-28 17:35:39.212843 UTC**；根和本课题 README 均与已读 blob 相同。

[小回执](../notes/2026-11-28-unit211-W-positive-e-k-minus-two-entire-ell-pole-actual-small-receipt-8542.json)保存实际原始阶段、source SHA、内层 exit 与原式范围。

结合 §3—§6，这次完成的是整个 ell 极点，而不只一般中心。与此前正 ell 排除合并，正 e、k 剩余值负二在当前分析中只余 **ell 单位**。其有限 mu、特殊 L 和 mu 极点须由各自完整原式继续；本稿不提前关闭它们，也不提前宣告整个 W 或普通 ISP 完成。
