# R224 — 单径向原像、全深 Euler–Hasse 观测与实际跨块关系格

日期：2026-11-13。**状态：原有理角参数的全深小成本运输、固定齐次块的准确 Smith、完整跨块关系格、角阶 Pascal 除幂整族，以及同一前缀中 Euler ladder 与全部加权原 Hasse jets 的整等价均已证明。原径向函数的固定仿射微分方程已写明。尚未从原标量前缀低损失地恢复 Euler ladder，也未由双完整中央条件得到新的主阶收益；主课题未完成。**

本篇在 [R221](R221-full-depth-polar-source-and-sharp-inverse-graph-denominators.md) 的原极坐标上继续工作。这里的观测等价始终是同一原源上实际有限矩阵的整行关系，不把新增的偏导或 Euler 槽当成已观察的原标量数据。

## 1. 原参数、同一源与全深权

取
$$
 p=4r-1\ge19,\qquad O=\mathbf Z_p,\qquad v_0=-22,
 \qquad E_D=O[A,C]_{\le D}.
 \tag{1}
$$
原 $A(w)=w+\cdots$、$C(w)=v_0w^2+\cdots$。令
$$
 R_p=r(p-1)=\frac{p^2-1}{4},\qquad
 \delta_n=\left\lfloor\frac n{R_p}\right\rfloor,
$$
$$
 e_n=
 \begin{cases}
 0,&q=\lfloor n/r\rfloor=0,\\
 q+\lfloor(q-1)/(p-1)\rfloor,&q\ge1.
 \end{cases}
 \tag{2}
$$
R215 给 $e$ 单调、超可加，$\delta$ 也超可加且 $\delta\le e$。记
$$
 \mathscr B_e=
   \left\{\sum a_nw^n:v_p(a_n)\ge-e_n\right\},
 \qquad
 \nu_e(f)=\inf_n\{v_p([w^n]f)+e_n\}.
$$
其乘法、常数项为一的形式逆都保持整性。

原 theta–sigma 参数为 $s=b/a$，$a=\vartheta^4,b=\sigma^4$。固定原函数满足
$$
 A=e^{\Lambda(s)}\Pi(s),\qquad
 C=e^{\Lambda(s)}\Pi(s)\mathcal Z(s),\qquad
 \Lambda=17\log a,
 \tag{3}
$$
其中 $\Pi(s)=s+\cdots$、$\mathcal Z(s)=v_0s+\cdots$ 为固定有理函数。更明确地，记
$$
 H_1=1+4s+70s^2+4s^3+s^4,\qquad
 H_2=1+20s-26s^2+20s^3+s^4,
$$
$$
 Q_8=1+364s^2-1088s^3+1190s^4-1088s^5+364s^6+s^8.
$$
则原规范准确给
$$
 \Pi=\frac15s(1-s)^2(1+s)
       (1-2s+5s^2)(5-2s+s^2)H_1H_2,
$$
$$
 \mathcal Z=\frac{(1+s)Q_8}{(1-s)H_1H_2}-1.
 \tag{4}
$$
这些是 R214 证书使用的原函数，不是可自由选择的轴截面。

置
$$
 u=\frac C{v_0A}=\frac{\mathcal Z(s)}{v_0}=q(s),
 \qquad
 F=\frac{v_0A^2}{C}.
 \tag{5}
$$
于是
$$
 q(s)=s+\cdots\in O[[s]],\qquad q^{-1}(u)\in O[[u]],
$$
$$
 A=uF,\qquad C=v_0u^2F,\qquad
 F=e^{\Lambda(s)}R_0(s),\qquad R_0=\frac{v_0\Pi}{\mathcal Z},\quad R_0(0)=1.
 \tag{6}
$$
$u$ 是固定原有理角参数，$F$ 是唯一的原径向函数。本篇所有结论也适用于 $p=919$，不要求 R221 的 $\lambda=919/15$ 是单位。

## 2. 角换参的成本是 $\delta$，不是 $e$

R215 的原椭圆对数为
$$
 w=s\,\mathcal F(s)^4,\qquad
 \mathcal F(s)=\sum_{n\ge0}
   \frac{\binom{2n}{n}}{4^n(4n+1)}s^n.
 \tag{7}
$$
已证明 $\mathcal F\in\mathscr B_\delta$，严格逆也有相同偏移成本。由 $q,q^{-1}$ 整，复合得
$$
 \boxed{\quad
       u(w)/w\in\mathscr B_\delta,\qquad
       w(u)/u\in\mathscr B_\delta .
 \quad}                                                       \tag{8}
$$
两个常数项均为一。

**完整目标运输。** 对任意 $k$，同一原函数的 $w$、$u$ 归一系数
$$
 \bigl(p^{e_n}[w^n]g\bigr)_{n<k},
 \qquad
 \bigl(p^{e_n}[u^n]g\bigr)_{n<k}
 \tag{9}
$$
之间为 $GL_k(O)$ 的单位下三角变换。

**证明。** 若 $n\ge i$，(8) 给
$$
 v_p([u^n]w(u)^i)\ge-\delta_{n-i}.
$$
而
$$
 e_n-e_i\ge e_{n-i}\ge\delta_{n-i}.
$$
所以归一换参矩阵整，严格性给对角一；反向同理。这证明全部有限连续前缀、全部精度的同源等价。$\square$

首个跨带系数也准确可见。由 R215 的 $p\mathcal F_{R_p}\equiv-1\bmod p$，
$$
 p[w^{R_p}]\frac{u(w)}w\equiv4\pmod p,\qquad
 p[u^{R_p}]\frac{w(u)}u\equiv-4\pmod p.
 \tag{10}
$$
较低相对系数全整。因为 $q$ 的非线性项的首坏项至少再延后一阶，所以 (10) 只读取其线性项。这也说明不能把第一带整换参不加说明地延伸成全深普通整换参。

下文统一在 $u$ 参数上写
$$
                         J_n(g)=p^{e_n}[u^n]g.
$$
由 (9)，这些仍是原完整连续像。R215/R221 的强首项及 (8) 给
$$
                         F,\ F^{-1}\in\mathscr B_e,\quad F(0)=1.
 \tag{11}
$$
特别，乘 $F^t$ 对每个整数 $t$ 都在各有限归一目标上是整单位操作。它只可对明确指定的整个目标统一使用；不同齐次块分别使用不同 $t$ 时，不能据此宣称完整混合像已经分裂。

## 3. 每个固定齐次块的有限像准确可知

令 $E^{(m)}$ 为原总次数恰为 $m$ 的齐次块。其原基满足
$$
 A^{m-c}C^c=v_0^c u^{m+c}F^m,\qquad 0\le c\le m.
 \tag{12}
$$
在这个固定块上，目标乘 $F^{-m}$，再作单位 $v_0$ 缩放，准确得到单项式矩阵。因此：

**命题 1。** 固定 $m,k$ 时，$J_{<k}|_{E^{(m)}}$ 的非零 Smith 指数准确是
$$
                         e_{m+c}\quad(0\le c\le m,\ m+c<k).
 \tag{13}
$$
其余源列为零列。模 $p^N$ 的实际像 $I_m$ 满足
$$
 \operatorname{length}I_m
     =\sum_{\substack{0\le c\le m\\m+c<k}}(N-e_{m+c})_+.
 \tag{14}
$$
没有第一带、$m<p$ 或 $r>2D$ 限制。

## 4. 全部新增收益准确位于跨齐次块交集

现在取 $k>2D$，所有 $I_m$ 均放在同一个原目标
$T_{k,N}=(O/p^N)^k$ 内。定义
$$
 I_{\le m}=I_0+\cdots+I_m,\qquad
 \gamma_{m,k,N}=\operatorname{length}(I_m\cap I_{\le m-1})
 \quad(m\ge1).
 \tag{15}
$$
令 $M_D=\binom{D+2}{2}$，并记原有限像缺损
$$
 B_N(J_{D,<k})=NM_D-\operatorname{length}I_{\le D}.
$$
则有准确恒等式
$$
 \boxed{\quad
 B_N(J_{D,<k})
   =\sum_{m=0}^D\sum_{c=0}^m\min(N,e_{m+c})
         +\sum_{m=1}^D\gamma_{m,k,N}.
 \quad}                                                       \tag{16}
$$

**证明。** 逐次使用有限模的正合列
$$
 0\longrightarrow I_m\cap I_{\le m-1}
 \longrightarrow I_m\oplus I_{\le m-1}
 \longrightarrow I_{\le m}\longrightarrow0,
$$
再代入 (14)。$\square$

这没有对各块使用不同目标后再相加。各块单独的单位操作仅用于求 (14)；(15)—(16) 始终在最初同一个目标中成立。若原 $J$ 未满列秩，$B_N$ 还包含准确核造成的 $N$ 项；在真正满秩前缀中，它就是全部截断 Smith 之和。

第一项满足
$$
 \sum_{m,c}\min(N,e_{m+c})
       \le\sum_{m,c}e_{m+c}=O(D^3/p).
 \tag{17}
$$
所以在 R223 的 $p\asymp D^2$ 区间，充分大 $D$ 时全部 $m+c<r$，第一项准确为零。这里每个齐次块都是原始的，全部实际收益均来自 (15) 的跨块关系；单独齐次块的中央换参不能产生它。

## 5. 固定角阶的 Pascal 原深核整族

另按角阶 $\ell=a+2c$ 分原源。固定 $0\le\ell\le2D$，记
$$
 a_\ell=\lceil\ell/2\rceil,\qquad
 b_\ell=\min(\ell,D),\qquad q_\ell=b_\ell-a_\ell+1.
$$
该块的原单项式经单位 $v_0$ 缩放后正是
$$
                        u^\ell F^m,\qquad a_\ell\le m\le b_\ell .
$$
令 $X=F-1$，改用
$$
 Q_{\ell,j}=u^\ell F^{a_\ell}X^j,\qquad 0\le j<q_\ell.
 \tag{18}
$$
这仍是原 $E_D$ 中的多项式。具体为
$$
 Q_{\ell,j}
 =\sum_{i=0}^j(-1)^{j-i}\binom ji
    v_0^{a_\ell+i-\ell}
    A^{\,2(a_\ell+i)-\ell}C^{\,\ell-a_\ell-i}.
 \tag{19}
$$
指数均非负，原总次数至多 $b_\ell\le D$；变基是整数 Pascal 单位矩阵。因此全部 $Q_{\ell,j}$ 是原源的一组整单位基，每个都在原源中 primitive。

R221 已证明 $X^j\in p^{v_p(j!)}\mathscr B_e$。结合 (11) 得
$$
 \boxed{\qquad
 \nu_e(Q_{\ell,j})\ge e_\ell+v_p(j!),\qquad
 J_{<k}Q_{\ell,j}\in p^{e_\ell+v_p(j!)}O^k
 \quad\text{对每个 }k.
 \qquad}                                                       \tag{20}
$$
所以这是实际完整前缀中的深核整族，未使用完整中央零。

全部列共同给出整化源
$$
 \mathcal D_D^{\mathrm{PD}}
   =\bigoplus_{\ell,j}
       O\,p^{-e_\ell-v_p(j!)}Q_{\ell,j}.
 \tag{21}
$$
它包含 R221 的原对角源 $\mathcal D_D$，且准确额外指数为
$$
 \operatorname{length}(\mathcal D_D^{\mathrm{PD}}/\mathcal D_D)
   =S_{p,D}:=\sum_{\ell=0}^{2D}\sum_{j=0}^{q_\ell-1}v_p(j!)
   =\sum_{j=1}^{\lfloor D/2\rfloor}(2D-4j+1)v_p(j!).
 \tag{22}
$$
最后一个等号使用 $q_\ell\ge j+1$ 当且仅当
$2j\le\ell\le2D-2j$。

在有限精度中，列的准确可证整除性给
$$
 B_N(J_{D,<k})
       \ge\sum_{\ell,j}\min\{N,e_\ell+v_p(j!)\}.
 \tag{23}
$$
若 $k>2D$，与 (16) 合并，得到同一个真实混合目标中的正向下界
$$
 \boxed{\quad
 \sum_m\gamma_{m,k,N}\ge
 \sum_{\ell,j}
 \bigl(\min\{N,e_\ell+v_p(j!)\}-\min\{N,e_\ell\}\bigr).
 \quad}                                                       \tag{24}
$$
式 (23) 只用每个原基列的像阶上界，不要求这些像列独立。

必须支付其规模。由 $v_p(j!)\le j/(p-1)$，
$$
                         S_{p,D}=O(D^3/p).
 \tag{25}
$$
并且 $p>D/2$ 时 (22) 准确为零。对全部素数求和可直接用阶乘分解：
$$
 \sum_p S_{p,D}\log p
   =\sum_{j\le D/2}(2D-4j+1)\log(j!)
   =\frac1{12}D^3\log D+O(D^3).
 \tag{26}
$$
限制到本篇惰性素数只会减少该量。

所以这一完整 Pascal／除幂整族确实给原深核和原跨块交集，但总预算只有 $O(D^3\log D)$；在所需的大素数 $p\asymp D^2$ 上，其 factorial 新层完全不存在。它不提供 R223 所需的对数深度主项。

## 6. 同一前缀的 Euler–角向整观测

在原源上定义两个交换的整数算子
$$
 \mathcal E=A\partial_A+C\partial_C,\qquad
 \mathcal L=A\partial_A+2C\partial_C.
 \tag{27}
$$
它们在 (12) 上分别有本征值 $m$ 和 $m+c$。所有
$\binom{\mathcal E}{i}$、$\binom{\mathcal L}{j}$ 都保持原整源。

取任意有限 $h,k$。考虑同一个原源上的两个实际矩阵
$$
 \mathfrak E_h(P)=
    \bigl(J_{<k}\binom{\mathcal E}{i}P\bigr)_{0\le i\le h},
$$
$$
 \mathfrak M_h(P)=
    \bigl(J_{<k}\binom{\mathcal E}{i}
                       \binom{\mathcal L}{j}P\bigr)_{i+j\le h}.
 \tag{28}
$$

**定理 2。** 这两个矩阵生成相同的整行模。$\mathfrak M_h$ 的附加行可用 $\mathfrak E_h$ 的行整消去；因此在每个 $p^N$ 层有相同的原源核和自然同构的有限像。证明不损精度，不读取第 $k$ 行之后的数据，也不要求 $h<p$。

**证明。** 使用真正角参数 $u$，定义共同目标算子
$$
 \mathcal T_t g=[v^t]g((1+v)u).
$$
在归一系数上它准确是对角算子
$$
                  (\mathcal T_t Jg)_n=\binom nt(Jg)_n .
 \tag{29}
$$
所以对所有 $t,k$ 都整且前缀封闭。这是 Hasse 系数，没有将普通导数的 $t!$ 当作单位。

再置
$$
 B(v,u)=\frac{F((1+v)u)}{F(u)}-1
            =\sum_{t\ge1}B_t(u)v^t,\qquad
 b_{i,t}=[v^t]B(v,u)^i .
 \tag{30}
$$
式 (29) 给 $\mathcal T_tF\in\mathscr B_e$，由 (11) 和超可加性，
所有 $B_t,b_{i,t}$ 都属于 $\mathscr B_e$。这里 $B(0,u)=0$，所以
$b_{i,t}=0$ 当 $t<i$；另有 $b_{0,0}=1$、$b_{0,t}=0$ 对 $t>0$。

乘任意 $b\in\mathscr B_e$ 的第 $(n,a)$ 个归一系数为
$$
             p^{e_n-e_a}[u^{n-a}]b\in O\qquad(n\ge a),
 \tag{31}
$$
因为 $e_n-e_a\ge e_{n-a}$。故 (30) 的每个乘法算子也整且前缀封闭。

将同一原函数的 $(F,u)$ 换为
$(F(1+B),(1+v)u)$，得到准确源恒等式
$$
 \mathcal T_t JP
   =\sum_{\substack{i,j\ge0\\i+j\le t}}
          M_{b_{i,t-j}}\,
             J\binom{\mathcal E}{i}\binom{\mathcal L}{j}P.
 \tag{32}
$$
右侧 $i=0$ 只有 $j=t$ 一项，系数是一；其余项的角向阶 $j<t$。
所以可以按 $j$ 三角消元。

更明确地，对 $Q=\binom{\mathcal E}{a}P$ 应用 (32)，便可从
$J\binom{\mathcal E}{a}P$ 和较低角阶读出
$J\binom{\mathcal E}{a}\binom{\mathcal L}{t}P$。
出现的 Euler 乘积满足整数恒等式
$$
 \binom Xi\binom Xa
      =\sum_{\nu=\max(i,a)}^{i+a}c_{i,a,\nu}\binom X\nu,
 \qquad c_{i,a,\nu}\in\mathbf Z.
 \tag{33}
$$
它可以按两个子集的并集大小计数，故不需除任何阶乘。
每个读到的项仍满足
$\nu+j\le a+i+j\le a+t$。因此对所有 $a+t\le h$，归纳始终留在同一个总阶 $h$ 的三角形中，最终只使用 $\mathfrak E_h$。

反向包含是 $j=0$ 的直接子行。所有操作已由 (29)、(31) 支付，所以结论在每个 $k,N$ 上成立。$\square$

## 7. 全部加权原 Hasse jets 也恰是同一 Euler ladder

定义实际加权原 Hasse 族
$$
 \mathfrak H_h(P)=
 \left(
 J_{<k}\bigl(
   A^aC^b\partial_A^{[a]}\partial_C^{[b]}P
       \bigr)
 \right)_{a+b\le h}.
 \tag{34}
$$
这里各项先在同一个原 $P$ 上求导再求值，没有假定其前缀另行消失。

**定理 3。** $\mathfrak E_h,\mathfrak M_h,\mathfrak H_h$ 三个矩阵有相同整行模，因而同精度有限像自然同构。

**证明。** 原算子准确满足
$$
 A\partial_A=2\mathcal E-\mathcal L,\qquad
 C\partial_C=\mathcal L-\mathcal E,
$$
$$
 A^aC^b\partial_A^{[a]}\partial_C^{[b]}
  =\binom{2\mathcal E-\mathcal L}{a}
        \binom{\mathcal L-\mathcal E}{b}.
 \tag{35}
$$
整数值多项式
$\binom{2x-y}{a}\binom{y-x}{b}$ 的二维 Newton 展开系数都是整数，且只使用
$\binom xi\binom yj$、$i+j\le a+b$。证明是用原多项式在非负整数格上的有限前向差作为系数；广义整数二项式即使上标为负仍整，总次数界则使超出该三角形的差分为零。于是 (35) 的各行整地来自 $\mathfrak M_h$，再用定理 2。

反向由 Vandermonde 恒等式
$$
 \binom{\mathcal E}{i}
   =\sum_{a+b=i}
          A^aC^b\partial_A^{[a]}\partial_C^{[b]}
 \tag{36}
$$
直接给出。$\square$

### 7.1. 去掉 Hasse 单项式权的准确成本

令 $t=a+b$、$\ell=a+2b$。若要读取未加权
$\partial_A^{[a]}\partial_C^{[b]}P$ 的前缀 $<k-\ell$，定义
$$
 d_e(k,\ell)=
  \max_{0\le n<k-\ell}(e_{n+\ell}-e_n)
 \qquad(k>\ell).
 \tag{37}
$$
已知 $\mathfrak E_t(P)$ 模 $p^{N+d_e(k,\ell)}$，就能准确读取该未加权前缀模 $p^N$。

事实上，(34) 的对应原函数准确为
$$
 A^aC^b\partial_A^{[a]}\partial_C^{[b]}P
   =v_0^b u^\ell F^t
          \bigl(\partial_A^{[a]}\partial_C^{[b]}P\bigr)(u).
$$
先乘 $F^{-t}$，这是整单位目标操作；再除 $v_0^b u^\ell$，第 $n$ 行只读取原第 $n+\ell$ 行，并付出
$e_{n+\ell}-e_n$。这证明 (37)，没有额外的 $v_p(a!b!)$ 损失。

一个与 $k$ 无关的安全上界是，$\ell>0$ 时
$$
 d_e(k,\ell)\le
 t_\ell+\left\lceil\frac{t_\ell}{p-1}\right\rceil,\qquad
                          t_\ell=\lceil\ell/r\rceil.
 \tag{38}
$$
因为两下标的 $\lfloor n/r\rfloor$ 最多相差 $t_\ell$，(2) 的第二项最多再增加 $\lceil t_\ell/(p-1)\rceil$。$\ell=0$ 时成本为零。特别 $0<\ell<r$ 时成本至多二。

### 7.2. 半次数 Euler ladder 已足够：全 p 的准确 Smith

对所有 $p\ge19,D\ge0$，只要
$$
                    h\ge\lfloor D/2\rfloor,\qquad k>2D,
$$
$\mathfrak E_h$ 的 Smith 指数就准确是
$$
                         \{e_{m+c}:0\le c\le m\le D\}.
 \tag{39}
$$
同样适用于 $\mathfrak H_h$，忽略冗余零行。这是一个统一充分阈值，不声称它是给定原曲线、$p,k$ 下的最小 $h$。

**证明。** 按第 5 节的原角阶 $\ell$ 排列源列，并暂将第 $\ell$ 块的每列共同除以 $p^{e_\ell}$，只作为原矩阵的因子分解；这个除法的源指数始终保留在最后的对角因子中。因 (11)，所得整矩阵 $\mathsf K$ 的条目为
$$
 \mathsf K_{(i,n),(\ell,m)}
   =\binom mi\,v_0^{\ell-m}\,
      p^{e_n-e_\ell}[u^{n-\ell}]F^m
 \qquad(n\ge\ell),
$$
$n<\ell$ 时为零。其整性准确来自
$$
                    e_n-e_\ell\ge e_{n-\ell},
$$
而非将不同齐次块各换一个目标。原 Euler 矩阵就是
$\mathsf K\operatorname{diag}(p^{e_\ell})$。

对每个 $\ell$，选择真实目标行
$$
                (i,n)=(0,\ell),\ldots,(q_\ell-1,\ell).
 \tag{40}
$$
因为 $q_\ell-1\le\lfloor D/2\rfloor$，全部所选行都存在。按 $\ell$ 排列这些行和原列，得到块下三角方阵；第 $\ell$ 个对角块准确是
$$
 \left(v_0^{\ell-m}\binom mi\right)_{
          0\le i<q_\ell,\ a_\ell\le m\le b_\ell}.
$$
去掉单位 $v_0$ 因子后，其行列式是一。事实上，$m=a_\ell,\ldots,b_\ell$ 是连续整数，逐列作整数前向差，将该矩阵变为
$\binom{a_\ell}{i-j}$，是对角全为一的下三角矩阵。这个证明在所有 $p$ 上成立，不要求 $m<p$，也没有未支付的阶乘分母。

所选方阵共有 $\sum_\ell q_\ell=M_D$ 行，行列式为单位。因此 $\mathsf K$ 有整左逆，可以用整目标行操作变为
$\binom{I_{M_D}}0$。对原未除列的矩阵施加相同操作，准确得到
$\binom{\operatorname{diag}(p^{e_\ell})}0$，证明 (39)。定理 3 给加权 Hasse 版本。$\square$

因而从任意满足上述充分阈值的 Euler ladder 取 $i=0$ 块，投影到原标量 $JP$ 时，其准确有限像长度损失就是
$$
                   \sum_{m=1}^D\gamma_{m,k,N}.
 \tag{41}
$$
这是第 4 节关系格的另一份实际识别。不能将已恢复的 Euler 目标信息保留下来，同时宣称它已经由原单标量前缀观察到。若仍通过间距 $r$ 的稀疏径向行分离这些 Euler 阶，所需范围仍可能为 $r\lfloor D/2\rfloor$；本命题本身没有把该成本缩到原标量的 $K_D+1$。

### 7.3. 足够 Euler 层的准确观测指数

继续取 $h\ge\lfloor D/2\rfloor$、$k>2D$，按原单项式基记
$$
 D_e=\operatorname{diag}(p^{e_{a+2c}}),\qquad
 J=J_{D,<k},\qquad
                         \widehat J=JD_e^{-1}.
 \tag{41a}
$$
$\widehat J$ 是整矩阵；它是原已付对角源上的实际标量矩阵，而非另选的自由列。

第 7.2 节的证明给
$\mathfrak E_h=\mathsf K D_e$，其中 $\mathsf K$ 有整左逆，且这个左逆仅使用 (40) 中 $n\le2D$ 的真实行。因此对每一个原 $P=\sum P_{a,c}A^aC^c$，准确有
$$
 \boxed{\quad
 v_p\bigl(\mathfrak E_h(P)\bigr)
     =\min_{a+c\le D}
          \{v_p(P_{a,c})+e_{a+2c}\}.
 \quad}                                                       \tag{41b}
$$
左侧表示全部目标坐标赋值的最小值；这个最低值已经在所选的低 Euler 行中出现。零向量的赋值按 $+\infty$ 处理。

实际上，$\mathfrak E_h$ 的整行模恰好是 $D_e$ 的行模。每个更高 Euler 行、以及每个加权原 Hasse 行的第 $(a,c)$ 列，都被同一个 $p^{e_{a+2c}}$ 整除。因此这段充分长的 Euler ladder 已经整生成全部高阶 Euler 与加权原 Hasse 行，不只是它们具有相同的 Smith 列表。

**准确指数命题。** 若 $J$ 满列秩，则在同一完整前缀上存在精度一致的整观察
$$
                    p^c\mathfrak E_h=\mathsf U J,
                    \qquad \mathsf U\in M(O)
 \tag{41c}
$$
的最小整数 $c\ge0$，准确是 $\widehat J$ 的最大 Smith 指数。若 $J$ 不满列秩，则不存在有限的 $c$。

**证明。** 消去可逆于 $\mathbf Q_p$ 的对角因子 $D_e$，(41c) 等价于
$p^c\mathsf K=\mathsf U\widehat J$。因 $\mathsf K$ 有整左逆，这又等价于
$p^cI_{M_D}$ 的每一行都属于 $\widehat J$ 的整行格。满秩 Smith 形式中，最后一个条件准确是 $c\ge s_{\max}(\widehat J)$；秩不足时，该行格不可能包含任何 $p^cO^{M_D}$。$\square$

这个指数也可以用原实际向量表述。由 (41b)，任何实现 (41c) 的观察，对每个非零原 $P$ 都必须支付
$$
 c\ge
 v_p(JP)-\min_{a+c\le D}
                 \{v_p(P_{a,c})+e_{a+2c}\}.
 \tag{41d}
$$
当 $J$ 满列秩时，右侧在原 $P$ 中的最大值恰为
$s_{\max}(\widehat J)$：取 $\widehat J$ 的最高 Smith 向量，清掉 $D_e^{-1}$ 所需的有限分母，再约去原系数的共同 $p$ 因子即可；这两次共同缩放都不改变赋值之差。

特别，若 $P$ 在原源中 primitive 且 $JP\in p^TO^k$，则任何全 Euler 观察至少付
$T-e_{2D}$ 层。当 $r>2D$ 时全部源角权为零，这个必要成本就是 $T$。若非零 $P$ 的原标量前缀在特征零下准确为零，(41b) 仍给有限的实际 Euler 最低值，故提高 $p$ 精度不能恢复它，必须增加真实观察行。

本命题给的是全精度统一指数。对于单个低精度 $N$，已经被固有角权杀掉的输入列可能使截断观察更便宜，应按实际核包含检查；不能把这一低精度例外用于主区间的深层恢复。由 (41c) 读取未加权 Hasse 时，第 7.1 节还给一条明确的充分路径：另付 $d_e(k,a+2b)$，并把输出窗口缩为 $<k-a-2b$。

这个 $c$ 没有被证明小。它准确等于尚待研究的原 post-diagonal 最大 Smith；不能将它先假定为单位，或作为独立于原有限像的已付成本。

## 8. 原径向函数满足固定的仿射一阶方程

这里给出的不是可调整未来系数的模型，而是 (3)—(4) 的原函数方程。

令
$$
 \mathcal H(s)=\sum_{n\ge0}
       \frac{\binom{2n}{n}}{4^n(4n+3)}s^n .
$$
原 theta 对数恒等式给
$$
 \Lambda'(s)=17\,\frac{\mathcal H(s)}{\sqrt{1-s}},
 \qquad \Lambda(0)=0,\qquad \Lambda'(0)=17/3.
 \tag{42}
$$
由 $(4s\partial_s+3)\mathcal H=(1-s)^{-1/2}$，直接得到
$$
              4s(1-s)\Lambda''+(3-5s)\Lambda'=17.
 \tag{43}
$$
等价地，若 $\Lambda'=\sum d_ns^n$，则
$$
 d_0=17/3,\qquad
                 (4n+3)d_n=(4n+1)d_{n-1}\quad(n\ge1).
 \tag{44}
$$
这些初值固定了实际解。

置
$$
 \kappa=R_0'/R_0,\qquad
 B_0=17+4s(1-s)\kappa'+(3-5s)\kappa .
$$
由 $F=e^\Lambda R_0$，
$$
 \Omega=\frac{F'}F,\qquad
              4s(1-s)\Omega'+(3-5s)\Omega=B_0(s).
 \tag{45}
$$
$\kappa,B_0$ 均为固定有理函数。

再令
$$
 \chi(s)=\frac{s q'(s)}{q(s)},\qquad
 g(u)=\frac{uF_u(u)}{F(u)},\qquad \partial=u\frac d{du}.
$$
则 $\chi(0)=1$，并且
$$
 \boxed{\quad
                    \partial g=\alpha(u)g+\beta(u),
 \quad}                                                       \tag{46}
$$
其中右侧由 $s=q^{-1}(u)$ 代入
$$
 \alpha=\frac{1+s}{4(1-s)\chi}
                   -\frac{s\chi'}{\chi^2},\qquad
 \beta=\frac{sB_0}{4(1-s)\chi^2}.
 \tag{47}
$$
两者都属于 $O[[u]]$，且是固定有理函数经固定整代数换参所得。准确有
$$
 g(0)=0,\quad \alpha(0)=1/4,\quad
 g_1=\lambda=919/15,\quad \beta_1=3\lambda/4 .
 \tag{48}
$$
由 (11) 和整数 Euler 系数算子，$g\in\mathscr B_e$。

原标量观测的一阶恒等式因而是
$$
              \partial(JP)=J(\mathcal L P)+g\,J(\mathcal E P).
 \tag{49}
$$
它保留混合次数；没有将 $m$ 当作所有源列共同的标量。固定齐次块上才可以把 $\mathcal E$ 换成 $m$。

## 9. 原完全整初段也可能没有无损 Euler 投影

下面是一份原源的精确结构性反例；没有更换曲线或人为删除轴，也没有声称该素数满足双完整中央零。

取 $D=2,k=6,p=131$，故 $r=33$，所读全部行权 $e_0,\ldots,e_5$ 为零。原 conic
$$
 P=C+22A^2+\frac{919}{15}AC
                  +\frac{1257757}{381150}C^2
 \tag{50}
$$
在原源中 primitive，所有显示分母都是 $131$ 单位。由 (3)—(4)、(42) 作有限有理展开，准确得到
$$
 [s^j]P=0\quad(0\le j\le4),\qquad
 [s^5]P=\frac{17347962938}{70875}
        =\frac{2\cdot131\cdot6803\cdot9733}{3^4\,5^3\,7}.
 \tag{51}
$$
严格换参 $w=s+O(s^2)$ 保留这个首个非零系数。因此
$$
                          J_{<6}P\in131\,O^6.
$$
其原多项式模 $131$ 是
$$
                        C+22A^2+70AC+100C^2.
$$
但原 Euler 算子准确给
$$
             \mathcal E P=2P-C,\qquad [w^2]\mathcal E P=22,
 \tag{52}
$$
是单位。因此不存在仅从这个原标量前缀整地读取同一前缀 Euler 观测的算子。

还可以核定全部有限像。按源列 $(1,A,C,A^2,AC,C^2)$ 及行 $0,\ldots,5$ 排列，原方阵的行列式为
$$
                  \det J=\frac{184721109363824}{70875},
                  \qquad v_{131}(\det J)=1.
 \tag{53}
$$
删掉 $C$ 列后，前五行在 $(1,A,A^2,AC,C^2)$ 上的行列式是
$v_0^3$，为单位。所以原标量 Smith 准确为
$$
                              0,0,0,0,0,1,
$$
而完整 Euler ladder 的六个 Smith 指数由 (39) 全为零。
式 (41) 的真实关系格在这里准确有一层。

这也发生在 $p>4k$ 的完全整初段。因此 (46) 的原径向方程不能自动产生一个无分母的第二观测；实际混合关系的分母可以来自原分子算术，而非原 theta 行权。该例只排除普遍的无损恢复，没有排除支付准确损失后的投影，也没有排除在完整中央零假设下证明额外结构。

## 10. 剩余入口精确到哪一步

定理 2—3 解决的是
$$
 \text{同一原 Euler ladder}
        \ \Longleftrightarrow\
 \text{同一前缀的全部加权原 Hasse jets},
$$
并由 (37) 支付未加权 Hasse 的窗口和精度成本。式 (39)—(41) 进一步给了完整 ladder 的准确有限像及其标量投影关系格。

尚未证明的方向是
$$
                  \text{原单标量完整前缀 }JP
                    \ \longrightarrow\
                  \{J\binom{\mathcal E}{i}P\}_i
$$
的低损失观测。式 (49) 仍同时含 $\mathcal L$ 和 $\mathcal E$，所以不能解一条方程就免费读出 $\mathcal E P$；(46) 也不能先把第二方向当成独立可观察量。

在 $p\asymp D^2$ 时，(22) 的 factorial 新层为零，而 R223 要求随 $D$ 增长的真实深层跨块交集。若尝试用径向微分方程的标量消去算子、$p$ 曲率或逆 Wronskian 构造第二个观测，必须保留它们消耗的完整行数、全部分母以及非交换次序。现有稀疏径向分离可能需要 $rD$ 量级的行，不能自动缩为真正 $K_D+1=O(D^2)$ 的前缀。

因此 (46) 是一个固定原几何输入，(16)、(24)、(41) 是实际像和关系格；由双完整中央条件对这些跨块关系给出额外深度，仍未完成。

依赖：[R167](R167-closed-theta-sigma-plane-and-integral-dynamics.md)、
[R173](R173-full-depth-cm-carry-envelope-and-true-jets.md)、
[R188](R188-original-source-detection-and-integral-hasse-transport.md)、
[R189](R189-complete-central-hasse-families-and-weighted-core.md)、
[R199](R199-exact-first-band-exponential-and-complete-divided-image.md)、
[R209](R209-coherent-source-reduction-and-mixed-euler-schur-image.md)、
[R214](R214-quadratic-pair-tail-recursion-and-deleted-c-image.md)、
[R215](R215-full-depth-faber-transport-and-first-cross-band-carry.md)、
[R218](R218-all-degree-original-image-intersection-recursion.md)、
[R221](R221-full-depth-polar-source-and-sharp-inverse-graph-denominators.md)、
[R223](R223-large-prime-deep-smith-and-original-product-input.md)。
