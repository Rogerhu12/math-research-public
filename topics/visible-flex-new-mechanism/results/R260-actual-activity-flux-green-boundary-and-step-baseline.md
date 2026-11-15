# R260：真实活动通量的 Green 边界式与非零常端基准

日期：2026-11-15。**完整纸面证明。** 本文只消费 R258 已证明的原函数恒等式，没有执行新的原根恢复、profile 评价、求积、正规化或矩阵消元。

新增结论是：对 R258 的十个完整第三对角核方向，R225 的真实截左通量可以直接写成两个端点的准确 Green 边界值。这个式子保留实际右尾，尤其保留 step 圆非零常平台处的基准。它省去这部分通量的额外积分，不自动支付内部 Laurent、两端 germ 或第四 ruling。

来源：[R225](R225-complete-period-range-flat-end-germs-and-finite-observation-quotient.md)、[R255](R255-explicit-third-diagonal-kernel-and-complete-hook-response-formula.md)、[R258](R258-self-adjoint-hook-green-operator-and-complete-period-interface.md)。

## 1. 已付的完整算子，不更换积分锚

固定一个真实光滑 seed f，全部原积分使用共同右 collar。对
$$
\tau\in Z_{71}=\mathfrak H_7\oplus\mathfrak J_3
$$
置
$$
K_f^\tau(w)=\tau(w;f,f),\qquad
G=K_f^\tau(w).
$$
R258 已证明完整身份
$$
G'''=\mathscr A_f^\tau w,\qquad
(\mathscr A_f^\tau)^*=\mathscr A_f^\tau,\qquad
\mathscr A_f^\tau f=0,
\tag{1}
$$
其中 $\mathscr A_f^\tau$ 是至多四阶的局部微分算子，系数二次依赖 f 的有限 jets。实际恢复为
$$
G=-\mathcal J^3\mathscr A_f^\tau w,\qquad
\mathcal J a(x)=\int_x^{r_*}a(\xi)\,d\xi.
\tag{2}
$$
原 $G,G',G''$ 在共同右 collar 全为零；其余平台上的二次多项式尾不删除。

w 可为在 I 上光滑、带真实左多项式尾的 $\Phi_E(D)$。下文的 Green 身份本身只用 w 光滑；涉及全区间无边界积分时，由 f 的全平零 collar 支付边界，不要求 w 左端为零。

每个实自伴至多四阶算子均可唯一写为
$$
\mathscr A w=D^2(aD^2w)+D(bDw)+cw.
\tag{3}
$$
例如从 $\mathscr A=\sum_{j=0}^4a_jD^j$ 可读
$$
a=a_4,\qquad b=a_2-D^2a_4,\qquad c=a_0.
$$
自伴性恰保证 $a_3=2Da_4$ 及 $a_1=Db$。当实际阶数低于四时，同一公式允许 $a=0$。这里 a,b,c 是微分算子系数，不是活动区间的端点。

## 2. 准确 Green concomitant

定义双线性边界式
$$
\boxed{
\begin{aligned}
\mathfrak B_{\mathscr A}(v,w)
={}&v(aw'')'-v'aw''
-w(av'')'+w'av''\\
&+b(vw'-wv').
\end{aligned}}
\tag{4}
$$
所有乘积和导数都在同一查询点 x；尤其 $(aw'')'$ 包含系数 a 的导数。

逐项微分可得
$$
\boxed{
D\mathfrak B_{\mathscr A}(v,w)
=v\,\mathscr Aw-w\,\mathscr Av.
}
\tag{5}
$$
证明只需把四阶部分写为
$$
\begin{aligned}
D\{v(aw'')'-v'aw''\}&=v(aw'')''-v''aw'',\\
D\{-w(av'')'+w'av''\}&=-w(av'')''+w''av'',
\end{aligned}
$$
中间两项准确相消；二阶部分的微分为
$v(bw')'-w(bv')'$，零阶部分 $cvw-cwv$ 为零。因而 (5) 不是忽略边界后的形式缩写，而是完整点态微分恒等式。

代 $v=f$ 并用 (1)，
$$
D\mathfrak B_{\mathscr A}(f,w)=f\,\mathscr Aw=fG'''.
\tag{6}
$$

## 3. 任意真实活动区间的截左通量

为避免与 (3) 的系数 a 混同，记一个 R225 活动区间为 $(\ell,u)$。定义其真实截左通量
$$
F_\ell(x)=\int_\ell^x f'(\xi)G''(\xi)\,d\xi.
\tag{7}
$$
令
$$
\Lambda_f^\tau(w)(x)
=f(x)G''(x)-\mathfrak B_{\mathscr A_f^\tau}(f,w)(x).
\tag{8}
$$
由 (6) 得
$$
D\Lambda_f^\tau(w)
=f'G''+fG'''-fG'''=f'G''.
$$
因此
$$
\boxed{
F_\ell(x)=\Lambda_f^\tau(w)(x)-\Lambda_f^\tau(w)(\ell).
}
\tag{9}
$$
特别地，该活动区间的总通量条件准确等价于
$$
\boxed{\Lambda_f^\tau(w)(u)=\Lambda_f^\tau(w)(\ell).}
\tag{10}
$$

式 (9) 的左端常数由真实活动左端确定。不能把 $\int_\ell^x$ 偷换为从全带左 collar 开始的积分，也不能只保 $\Lambda(x)$ 而删去 $\Lambda(\ell)$。式 (2) 的右锚仍完全保留在 $G''$ 中；这里没有引入新的独立 primitive 或自由端点常数。

在 R225 的记号
$$
p=f',\qquad A_H=6f'f'''-2(f'')^2
$$
下，内部 Green 商的真实分子可直接写为
$$
q_\ell(x)=
\frac{\Lambda_f^\tau(w)(x)-\Lambda_f^\tau(w)(\ell)}
     {A_H(x)\,p(x)^2}.
\tag{11}
$$
(11) 只在分母不为零处使用；内部零点仍按 R225 的 Laurent 消极点、禁 residue 和拼接规则处理。分子是已由 (9) 证明的真实光滑函数，不能因为它有边界表示，就预先取消分母的某个零点。

## 4. 非零常平台的基准必须保留

假设 f 在活动左端的左侧为常数 $f_0$，并且在 $\ell$ 全 jet 平接。因此 $f'(\ell)=f''(\ell)=\cdots=0$。从 (4) 得准确端值
$$
\mathfrak B_{\mathscr A}(f,w)(\ell)
=f_0\{a'(\ell)w''(\ell)+a(\ell)w'''(\ell)+b(\ell)w'(\ell)\}.
\tag{12}
$$
故
$$
\boxed{
\Lambda_f^\tau(w)(\ell)
=f_0\{G''(\ell)-a'(\ell)w''(\ell)
-a(\ell)w'''(\ell)-b(\ell)w'(\ell)\}.
}
\tag{13}
$$

若 w 在这个平台本身是二次多项式，只有 $w'''(\ell)=0$ 可以据实删除。其余项仍须保留。即使已经另行支付平台门 $G''=0$，式 (13) 中的 Green 边界项也未必为零。

对旧 step 圆，f 在某些活动区间两端可有不同的非零常值，所以 (10) 是两边准确端值的相等，不是两个端值分别为零。尤其不能由全 I 上的 $\int f'''G=0$ 推每个活动区间总通量为零；R219 的非零局部通量与本结论并无冲突。

在 R258 的未递推最低方向 $\mathfrak J_0$ 或 $\mathfrak H_0$，f 为常数时其 a,b 均为零，(13) 简化为 $f_0G''(\ell)$。但对整条 $\delta$ 串，不使用这个额外简化；准确规则始终是 (12)–(13)。

## 5. 整 profile 微包的范围更强

若
$$
f=\sum_i a_i u_i
$$
且 $u_i$ 的完整紧支撑两两不交、包界全平，令 $f_i=a_i u_i$。在每个非零包内部 $f=f_i$，包外 $f_i$ 及全部 jets 为零。局部性、二次齐次性及 $\mathscr A_f^\tau f=0$ 给
$$
\mathscr A_f^\tau f_i=0.
\tag{14}
$$
用 $f_i$ 代入 (4)–(9)，其真实两端均为零端而非非零常端，所有边界项为零。因此
$$
\boxed{
\int_{\operatorname{supp}u_i}f'G''
=\int_{\operatorname{supp}u_i}f_i'''G=0.
}
\tag{15}
$$
这与 R258 的逐包证明一致，现有 (9) 给出其真实点态 primitive。

若每个 $u_i$ 内部解析、无内部开常平台、只有有限内部临界点，则每个完整包就是 R225 的一个活动区间，(15) 支付所有该类活动总通量门。内部临界点和 $A_H$ 的零点仍须作 R225 的独立局部处理。

若一个包内部还含非零常平台，则整包 (15) 不能替代把它拆开的各活动通量条件。旧 R225 step 类恰不能随意套用该加强。

## 6. 两个完整 mixed 响应仍保历史项

采用 R258 的准确规范
$$
\mathcal B_E(\tau)=\sin^2\theta\,D_{E,\tau}
+\cos\theta\sin\theta\,E_{E,\tau}.
$$
置
$$
u_d=\Phi_E(f^2-g^2),\qquad u_e=\Phi_E(fg),\qquad
\zeta=K_f^\tau(g).
$$
完整两个目标为
$$
D_{E,\tau}=2K_f^\tau(u_d)+4\Phi_E(g,\zeta),
$$
$$
E_{E,\tau}=-4K_f^\tau(u_e)+4\Phi_E(f,\zeta).
\tag{16}
$$
因此在任一活动区间，真实截左通量准确为
$$
\boxed{
\begin{aligned}
\int_\ell^x f'D_{E,\tau}''
={}&2[\Lambda_f^\tau(u_d)]_\ell^x
+4\int_\ell^x f'\{\Phi_E(g,\zeta)\}'',\\
\int_\ell^x f'E_{E,\tau}''
={}&-4[\Lambda_f^\tau(u_e)]_\ell^x
+4\int_\ell^x f'\{\Phi_E(f,\zeta)\}''.
\end{aligned}}
\tag{17}
$$
式 (17) 没有把第二项视为零。只有先由原式证明 $\zeta=0$，例如 R258 的整 profile 逐包比例类，才可删这两条真实历史项。

若使用另一常用规范
$V_\theta=\sin^2\theta V_d+2\cos\theta\sin\theta V_e$，
则 (16) 的 E 列对 $V_e$ 的贡献是 $E_{E,\tau}/2$，不能漏此二分之一。活动通量和 R225 的全部观测保持线性，但这不是实际带符号成本已经实现的结论。

## 7. 已完成与仍须联合支付的部分

(9) 与 (17) 给出完整原函数的准确有限端值/历史接口。对具体固定圆和有限控制基，可以据此组装活动总通量的线性观测，不再为这些 K 项新求一遍积分，也无需重编已付原 forcing 或重复 $\Delta\tau$。

完整 period 仍要求同一个修正元素同时满足：

- 每个真实常平台上的 $G''=0$，并保共同右 collar 的两个积分常数；
- 每个活动区间的准确总通量；
- 所有内部退化点的 R225 Laurent 条件；
- 两个平端 germ 的光滑延拓与真实拼接。

本稿只把第二项中 R258 的 K 贡献精确化；没有删除其余三类门，没有证明全部响应像满射，也没有处理同一 gauge 的第四 ruling。八个额外 $\chi_j$ 的局部性/自伴性仍由独立新目标判定；不能在该判定前把本文定理称作整个十八维 Z 的结论。

作者责任：全部新证明为有限微分与同锚分部积分的纸面推导。没有运行新研究计算或新人工检查。

