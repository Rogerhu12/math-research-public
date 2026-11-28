# R150：完整原 N4(V) 的已付 M 四次降幂、两列返回与两条新必要标量

日期：2026-11-28（Asia/Taipei）。
会话：Astra-ISP-8542378f-20261127。

## 1. 原域与实际结论

本篇仍在当前 W、两个 singleton 原值互异的图内：
$$
D=\ell A_\lambda-T^2=bc(h_U-k_U)^2\ne0,\qquad
A_\lambda=2\lambda^2-2\lambda+1.
$$
全部纯权分母沿先行 W 原定理支付；尤其
$$
m=u-\ell,\quad \delta=1-Q,\quad M=4bc\delta
$$
在本图是单位。本篇不把这些结论外推到值碰撞图 $h_U=k_U$。

完整原 $N_4(V)$ 与已经证明的原四次 $C_4$ 给出一个新的、
几何次数至多四的必要式 $\overline B_4=0$。
其全部 native 均值来源、六个基元的短除以及新的两列返回
均在唯一首次正常运行中完成。随后两个固定原 pair 给出
$$
C_W(e,k,\chi)=0,\qquad C_O(e,k,\chi)=0,                   \tag{1}
$$
实际三次数及总次数分别为
$$
\deg_{e,k,\chi}C_W=(107,118,8),\quad\deg_{\rm tot}C_W=178,
$$
$$
\deg_{e,k,\chi}C_O=(109,119,8),\quad\deg_{\rm tot}C_O=180. \tag{2}
$$
两式分别有 $69382,70992$ 项，均非零。
它们只是同一点原解的必要条件；没有据此宣称新纯权覆盖、
有限性或当前 W 排空。原 $b_\Delta=0$、所有未付 $\chi$ 首项与
实际乘子公因子零面完整保留。

## 2. 完整原值的 D 降幂身份

先行
[两个原四次](R150-appendix-unit211-W-original-two-quartic-necessary-values.md)
和
[完整 N4(V) 的低 D 理想压缩](R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)
给出
$$
C_4=2mD\,a_\Delta+K b_\Delta,\qquad
\ell^2V_{\rm low}
 =D\widetilde Z_0+\frac K{2m}\widetilde Z_1
                    +\frac{D^2}{M}\widetilde Z_2,        \tag{3}
$$
其中
$$
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,\qquad
K=\ell^2B_\lambda-3\ell A_\lambda T+2T^3.
$$
这里 $V_{\rm low}$ 保留完整原 $N_4(V)$ 必要条件；
它不是某一个分量，也不是用未付 $\Phi$ 的倍数替代原式。

令 $c_\lambda=3-2\lambda$、$w=\lambda-1-T$，
$V=bX+cY$、$W_1=bpX+cqY$，$A_1$ 为原 double-germ Gram 对角。
独立的
[三个缩放完整 N4 短式](R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)
在九个自由原变量上已经逐项证明
$$
\begin{aligned}
\widetilde Z_0={}&\ell^2A_1+4\ell^2(1-2\lambda)f+2\ell fD\\
 &+2\ell u w(\ell c_\lambda+T)
 +2V(\ell^2+\ell c_\lambda T+T^2)
 +2bc\,t(T^2-\ell^2),\\
\widetilde Z_1={}&2(\ell c_\lambda+2T)(uV-\ell W_1)
                 -2\ell Mw+4bc\,mTt,\\
\widetilde Z_2={}&2\{(u^2-\ell^2Q)V-2m\ell W_1-\ell Mf-bcMt\}.
\end{aligned}                                          \tag{4}
$$
这份先行一般身份使用真正的 germ 乘法，
未依赖错误 compact 均值；本次直接引用，不重跑其已成证书。

写
$$
A_*=4uQ-J,\qquad C_*=A_*m^2+J\delta\ell^2.
$$
原四次的两个系数为
$$
\begin{aligned}
a_\Delta={}&M\ell^2Q(3-4\lambda)+MA_*T^2
         +2MuQc_\lambda\ell T+DC_*,\\
b_\Delta={}&2Mm(A_*T+uQc_\lambda\ell).
\end{aligned}                                          \tag{5}
$$

在原 native 坐标 $X=x+\rho y,\ Y=x-\rho y$、
$\rho^2=\delta$ 中，完整线性恒等式为
$$
V=\ell x+my,\qquad uV-\ell W_1=-My.                      \tag{6}
$$
定义
$$
\begin{aligned}
b_0&=2m(A_*T+uQc_\lambda\ell),\\
z_1&=-2(\ell c_\lambda+2T)y-2\ell w+\frac{mTt}{\delta},\\
z_2&=2\{\ell(x-f)-my-bc\,t\}.
\end{aligned}
$$
实际原乘回给出
$$
b_\Delta=Mb_0,\qquad \widetilde Z_1=Mz_1,\qquad
\widetilde Z_2=Mz_2.                                   \tag{7}
$$
这里只约掉已有纯权单位 $M$，没有倒任何几何首项。

真正的新输入是
$$
\overline B_4=b_0(\widetilde Z_0+Dz_2)-a_\Delta z_1.     \tag{8}
$$
由 (3) 与 (7) 逐三个形式系数直接得到
$$
(2m\ell^2b_0)V_{\rm low}-z_1C_4=2mD\,\overline B_4.     \tag{9}
$$
本次源实际返回了 (6)、(7) 和 (9) 的全部三个形式系数。
因为当前原图 $mD\ne0$，所有原解都满足 (8) 等于零。
整个 $b_0=0$，即 $b_\Delta=0$ 纤维也满足这一必要结论；
证明从未倒置 $b_0$。也没有宣称以 (8) 替换
$V_{\rm low}$ 后得到一个充分或等价的原系统。

在 $(x,y,t)$ 中，$f,\lambda,T,V,W_1,A_1$ 都仿射；
(4) 与 (5) 给出 (8) 的总几何次数至多四。
本次对实际完整分子核实了这个次数。
相比原 $V_{\rm low}$ 中的五次项，此处通过真正原 $C_4$
组合先降幂，再进入归约器。

## 3. 新四次的完整 native 来源

取固定六列
$$
\mathbf b=(1,x,y,t,y^2,yt)^t.
$$
正确旧 C9 原归约器只对本次新 $\overline B_4$ 调用一次，实际得到
$$
\mathbf r\mathbf b-\overline B_4
 =\sum_{j=0}^{3}\tau_jF_j,                               \tag{10}
$$
其中 $F_j$ 是同一点的四条原均值。
完整来源的 NS、PS 两个坐标均为零，旧归约器的权分母白名单
保持不变并全部通过。此处没有把六个生成元当成自由基。

(10) 在 $86.374723891$ 秒完整返回，
六列规范定义为 $1330815$ 字节、SHA256
cb05ed84a2c2d9d6f486cc3c90e649f314eec61c26ff6c79650728abbcd758be。
仅保此定义与小摘要，未保存可重算载荷。
旧十二个 $\lambda/T$ 动作、完整五次值换基、旧余子式或范数
均未在本次执行。

## 4. 六基元一次短除，保原来源的两列收缩

先行
[完整 alpha/chi 原图](R150-appendix-unit211-W-alpha-chi-exact-original-ten-by-two-and-three-scalars.md)
给出纯权分母的可逆坐标及
$$
q_\alpha=\alpha^2+q_1(e,k,\chi)\alpha+q_0(e,k,\chi)
\in I_4.                                               \tag{11}
$$
本次仅取其定义前缀，不重跑旧十行或旧三个标量。

每个 $b_i$ 在 $\alpha$ 上次数至多二。
用一个共同纯权单位 $D_B$ 清分母后，六个完整身份为
$$
D_B b_i=B_{i0}+B_{i1}\alpha+H_iq_\alpha,\qquad 0\le i<6.
                                                               \tag{12}
$$
本次实际返回十二个非平凡系数乘积；
六个 $\alpha^2$ 系数由 (11) 的首一性对应。
不是十八次独立展开，也没有添加新的 $\chi$ 首项逆。

另以共同纯权单位 $D_R$ 清 (10) 中六个 $r_i$ 的分母，
令 $r_i'=D_Rr_i$。定义多项式收缩
$$
B_j'=\sum_i r_i'B_{ij},\qquad H'=\sum_i r_i'H_i .
$$
逐个收缩 (12) 的实际乘回，与 (10) 合成
$$
D_BD_R\,\overline B_4
 =B_0'+B_1'\alpha+H'q_\alpha
   -D_BD_R\sum_j\tau_jF_j.                              \tag{13}
$$
这保留了同点原来源 DAG。
完整证据是已经实际成立的六个多项式身份的线性组合，
不要求再把巨大有理式重新统一分母展开为一个额外门。

仅从两列公共内容剥已付纯权因子，得
$$
(B_0',B_1')=U_B(B_0,B_1),\qquad U_B\ \text{为已付权单位}.
                                                               \tag{14}
$$
本次按已付支持 $e,k,u,\delta,M,\ell$ 记录的 gcd 层数为 $1,1,3,1,1,2$；准确因子始终取实际回乘的剥除乘积，不将标签层数混同于未经核定的整因子幂。
所有未付内容均保留。实际两列参数摘要为

| 列 | $(e,k,\chi)$ 次数 | 总次数 | 项数 | SHA256 |
| --- | --- | ---: | ---: | --- |
| $B_0$ | $(106,117,7)$ |177|59924|2e0ddf68e6493223a6490f5f06b576490d0a9d294837cdc67d89b49922564c4c|
| $B_1$ | $(102,116,8)$ |174|64253|6f8728926bf9df9ed449815f4461638ea3efd7668786575e9a77452b12c49262|

所以 (13) 在 $91.745408046$ 秒给出完整原必要行
$B_0+B_1\alpha=0$。原其他均值、N1、NS、PS、
完整个别值条件仍全部保留。

## 5. 两个新原标量及乘子零面的覆盖

分别把原 $E_W$、原 $E_{Bo}$ 对同一首一 (11) 短除并只清已付权分母。
记所得任一行为 $(r_0,r_1)$，另一行为 $(B_0,B_1)$。
令
$$
g=\gcd(B_1,-r_1),\qquad
\mu=B_1/g,\quad \nu=-r_1/g.
$$
本次只精除两个实际乘子的共同内容，并完整返回
$$
\mu r_1+\nu B_1=0,\qquad
C=\mu r_0+\nu B_0
 =\mu(r_0+r_1\alpha)+\nu(B_0+B_1\alpha).                \tag{15}
$$
因此 $g$ 的零纤维也满足这个新的原多项式组合。
没有把原方程除以一个未付因子。

两对的 $g$ 均为双次数 $(1,1)$、总次数二、三项，
规范 $49$ 字节，SHA256
b5e2fb659b61bd523da5b359c23577c6ab76bf91db551c7621ec0785cba6bacf。
证明不需要把它识别为新的单位。

只剥 (15) 中已付纯权支持后，得到 (1)。
$C_W,C_O$ 的准确再生定义就是冻结源中的这两个固定 pair
及其实际合法剥除，不以数值采样或多元 gcd 给排空推断。

| 必要式 | 原 pair | 规范字节数 | SHA256 |
| --- | --- | ---: | --- |
| $C_W$ | 原 $E_W$ 与新 $\overline B_4$ |4285968|8b545db5323d321c6000d29fc37145d22ea28fe989647e1eb6857ab50ad9718c|
| $C_O$ | 原 $E_{Bo}$ 与新 $\overline B_4$ |4405386|0b72a9922aa1ba7ce607a10ac1a5576535c56acd53fdda7f566c41cdaccd94a2|

它们分别在 $107.639683602$ 与 $122.029137030$ 秒完整返回。
全部实际两列乘积均核实；没有新的权投影或共同零集结论。

## 6. 唯一正常首次运行与旧实现失败的区别

新冻结源：
[已付 M 的完整原四次两列](../notes/2026-11-28-unit211-W-full-NV-paid-M-quartic-original-two-columns-8542.py)；
[原输入与归约范围](../notes/2026-11-28-unit211-W-full-NV-paid-M-quartic-original-two-columns-8542-input.md)。

源 git blob 726554aef5069c14e0e86a1138cce6948a13b7a9，
$12108$ 字节，SHA256
dd576892e229c5b4c53d49cd8dc1fe941a640ff933983f14e0ae5372e6c77265。
仅依赖两个固定必要定义前缀：

- alpha/chi 原源 SHA256
  18101a4af587253e1dad49cee60d188c60db401ed34b13cf73edeb4e09b6d42b，
  取到旧十行之前的 $9855$ 字节，前缀 SHA256
  c1436ea6bb67d4c720016091fb65f439be5bfcc7af131c00a0749321fcf45e43；
- 正确 C9 原源 SHA256
  10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1，
  取旧乘法矩阵之前的 $14656$ 字节，前缀 SHA256
  88b8e2f49f925e51c0b940f929efb502ced9ed358228a605fea3755d9cdefff8。

唯一正常首次 run46124406408/job140915689273：
内层退出 $0$；驱动墙钟 $122.127592445$ 秒；
峰值 RSS $722168$ KiB；原限制 $180$ 秒、$4$ GiB。
全部 $94$ 个新精确多项式除法乘积、十二个实际基元系数身份、
完整四次原迹、两列收缩和两个新原标量均返回。
stdout $4995$ 字节，SHA256
b49efb8549d9392ab49cf26d9be931d7f146802dd9abc0d7dde808c3ad54bf8c。

源固定提交 ce00b012b6db58ea4b1c8125a005efe078cdce96。
真实 git pull 于 2026-11-28 08:08:40.400326 UTC
到 2ece92b92b5775dcbb7bfe17f32ad9e92ee52a41；
根及课题 README 都没有变化。
[完整小回执](../notes/2026-11-28-unit211-W-full-NV-paid-M-quartic-original-two-columns-receipt-8542.json)
保留各完成阶段、真实退出及参数摘要。

此前 97cf 源的 run46123468127/job140912794324
在建立 $W_1$ 时发生 TypeError：旧 C9 前缀末的变量名 q
已经表示六条归约规则，不能当作物理 $q$。
它在任何新四次或标量定义完成前退出，原失败记录独立保留。
本次从原 Gram 第一行读物理 $p,q$ 并核共轭，修正具体接口；
没有删断言、改写失败身份或重新运行一个已成数学目标。
17703 白名单失败与 2d722 旧值换基超时也保持冻结。

没有保存大系数、矩阵、编码载荷或分片。
(9)、(13)、(15) 是本篇的完整原来源；后续所有候选仍须满足
同一点的其余原条件。
