# R443 — 原 144 响应联合核的完整 self 像：唯一实际得到 38 维，加 K 链为 49 维

## 0. 结论与本次唯一新问题

2026-11-16 的唯一公开实际 [run 43801705436](https://github.com/Rogerhu12/math-research-public/actions/runs/43801705436)、job 133083261189 已成功完成。source 为 9c796878a2f7f1b910ebcebadd0b2d05dc0d42ac。

本次只消费 [R434](R434-complete-self-kernel-and-three-tail-current-image-on-144-original-responses.md) 已付的 18 个原算子、85 个 whole-Q 核列及其中 53 个三尾 current 依赖关系，首次计算这 **53 个准确原组合的完整 self 累计流**。没有重做原 18 算子构造、144 个 Q、原 Q/current 的秩或旧检查。

结果是：

| 本次完整新对象 | 准确结果 |
|---|---:|
| 53 列在 $A_f=0$ 处的完整 self-current 像 | 38 维 |
| 53 维输入系数空间中的 self 核 | 15 维 |
| 加入已付 $K_0,\ldots,K_{10}$ 后的 64 列像 | 49 维 |
| 此 64 维输入系数空间中的核 | 15 维 |
| 原 11 个非 K 参考方向 | 全部 MEMBER，完整残差为空 |
| 相对原已付 22 维模块的新形式方向 | 27 维 |
| 非局部词、高阶外 jet、$p$ 分母的残余 | 53 列全部为零 |

这里的“局部”准确指：**先恢复完整同右锚 current，再只在外部评价点施加 $A_f=0$，所得是局部多项式。** 不把这一结论改写成代入前的全 self 场本来局部。

本稿证明的是原响应模块在自由退化 jet 上的完整形式像。没有评价任何实际母包、镜点或固定根。因此不授 49 个实际点条件可以独立支付，也不继续把 [R440](R440-complete-zero-order-compatible-self-module-and-sixteen-actual-fluxes.md)、[R441](R441-nonzero-order-Wronskian-compensation-and-a-new-local-self-current.md) 的六个 mirror-blind 方向称为这个增广模块的完整余核。

## 1. 原算子、规范和输入来源

写

$$
p=u',\qquad r=u'',\qquad t=u''',\qquad
\mathcal A=6pt-2r^2,\qquad
I(g)(x)=\int_{r_*}^{x}g(y)\,dy=-J(g)(x).
\tag{1}
$$

$r_*$ 是全过程同一个真实右锚。原 18 个 third-diagonal 核算子，依 [R255](R255-explicit-third-diagonal-kernel-and-complete-hook-response-formula.md)、[R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md)，满足

$$
D^3K_{\tau,u}(w)
 =D^2(a_{\tau,u}w'')+D(b_{\tau,u}w')+c_{\tau,u}w,
\qquad
D^2(a_{\tau,u}u'')+D(b_{\tau,u}u')+c_{\tau,u}u=0.
\tag{2}
$$

本次直接读取原输出中的 $a,b,c$ 精确有理系数，不重新生成这些算子。标签保持

$$
H_0,\ldots,H_6,\quad J_0,J_1,J_2,\quad
\chi_{30},\chi_{32},\chi_{34},\chi_{37},
\chi_{40},\chi_{100},\chi_{104},\chi_{109}.
$$

八个内算子依原序为 $P,R,S,L,U,V,T,Y$；其中 $V=p_1,Y=p_2$，不是新改名的算子。144 个原响应均保 $B_E\tau$ 规范。

R434 的 53 个 dependent 记录是 **85 个已付 whole-Q 核列之间的三尾 current 关系**。不能把其 kernel_index 直接当成 144 原标签序号。本次按两层原组合准确展开：

$$
\mathbb R^{53}
 \longrightarrow \mathbb R^{85}
 \longrightarrow \mathbb R^{144}.
\tag{3}
$$

令第 $i$ 个展开后的响应为 $V_i$，$0\leq i\leq52$。本稿的 15 维核首先是映射 (3) 后 self-current 的**输入系数核**；不把它无条件等同为所有完整响应函数的核维数。

原输入绑定：

| 原 R434 记录 | 身份 |
|---|---|
| run / job | 43796872698 / 133067569306 |
| source | 563defb46bc785295265c3f48fcad3fc8897c617 |
| 原 stdout | 1,322,512 bytes；SHA256 1edd4dd8ac34e2a9fe6fc1cf7ae08dc2d91fa279c02e6c32365bff9830e013b1 |
| 1020-record JSONL | 1,170,464 bytes；SHA256 dd936dc713d3461cfbf2652c4e88c89ac4b918eb7949bb379f3b940d62cb8ec7 |
| 原记录链 | 673061557c1b53e78bf300d18e11e510d091378ad3431e159f6049404cde5101 |
| 原 request | 9,269 bytes；SHA256 fd6e8526d6f7e9492911848b17a852d64a31654513a267ba61e5bdb9390ffb01 |

原 stdout 与 request 只在 runner 内存读取。旧 whole_word_rows 是 whole-Q 的密度记录，**没有被当成 $I(c_\tau q_E)$ 的原函数**。

## 2. 完整 self-current 公式与真左常数

对一个原响应，置 $q_E=\Phi_E(u,u)$，并记

$$
h_\tau=(a_\tau r)'+b_\tau p.
$$

由 (2) 得 $h_\tau'=-c_\tau u$。真实同锚恢复是

$$
K_{\tau,u}(q_E)''
 =(a_\tau q_E'')'+b_\tau q_E'+I(c_\tau q_E).
\tag{4}
$$

完整 self 是 $2K_{\tau,u}(q_E)$。因此其从左 collar 累计到 $x$ 的 partial 流为

$$
\begin{aligned}
\mathfrak S_{E,\tau}(x)
&=\int_{\ell}^{x}p\,\{2K_{\tau,u}(q_E)\}''\,dy\\
&=2\left[
 a_\tau(pq_E''-rq_E')
 +q_Eh_\tau
 +uI(c_\tau q_E)
 \right].
\end{aligned}
\tag{5}
$$

微分右端，使用 $h_\tau'=-c_\tau u$，恰给左端密度。左 collar 上 $u,p,r$ 及算子局部系数平零，故积分常数准确为零；$q_E$ 的真实左二次尾和 $I(c_\tau q_E)$ 的左值都保留。没有假设 $q_E$ 左紧。

对 (3) 的组合，所有项先线性合并，实际执行的式子为

$$
2\left\{
 \sum\lambda_{E,\tau}a_\tau(pq_E''-rq_E')
 +\sum\lambda_{E,\tau}q_Eh_\tau
 +uI\!\left(\sum\lambda_{E,\tau}c_\tau q_E\right)
 \right\}.
\tag{6}
$$

(5)—(6) 是完整 $2K$ self 规范，不能沿用 ordered current 的 $K/4$ 读出。

**原锚处理。** 原 $J_0,J_1,J_2$ 以及所有后续 $I$ 都经同锚字表达处理。积分分部、同锚乘积和原多项式恒等式只作准确等式变换；不凭 moment zero 删除未付的单包尾。完整 current 在外部退化代入前也逐列输出。

## 3. 两个新 adapter 与忠实的退化评价域

新的两个开发检查只验证此次新增接口：

1. 一个发明的二次 self/同锚 Green 测例，含真正非局部 $w$，检查 (5) 的微分。
2. 一个外 Af 适配测例，同时含积分字内部 $t^2$、外部 $u^{(4)}$ 与外部 $t$。它必须只替换最后一种，并原样保留前两种。

二者都通过。旧开发检查没有执行。

定义

$$
F_i(x,u,p,r)=
 \left.\mathfrak S_{V_i}(x)\right|_{t=r^2/(3p)},\qquad p\ne0.
\tag{7}
$$

替换只作用**外部 jet**。不在任何积分字内部代入，不微分 $\mathcal A=0$，也不以此删除 $u^{(4)},u^{(5)},\ldots$。若还剩非局部词、高阶外 jet 或未处理表示，程序将保存并列为 unresolved，而不把表示非零自动判成函数非成员。

这次实际的 53 列均得到

$$
F_i\in\mathbb Q[x,u,p,r],\qquad
\deg_{u,p,r}F_i=5
\tag{8}
$$

（零列除外），所有 $p$ 分母阶数为零，所有非局部与高阶外 jet 列为空。原新 53 列的显式 $x$ 次数不超过 7；加 K 链后不超过 10。

此时系数坐标是忠实的：在 $p\ne0$ 的开放域，$x,u,p,r$ 可由真紧光滑 profile 的有限 jet 实现，随后指定 $t=r^2/(3p)$；若还要求该点是简单 $\mathcal A$ 根，可用 $u^{(4)}$ 调整，因为 $\partial\mathcal A'/\partial u^{(4)}=6p\ne0$。因此一个局部多项式恒为零，当且仅当全部系数为零。

这是自由 jet 的函数身份论证。它不把固定母包的 $u,p,r$ 当成独立变量，也不授原 19 值纤维或有限镜点的评价满秩。

53 个新的 Green 导数检查全部通过。实际报告中 fresh derivative mapper 的调用数是 0，因为这些导数差在准确表达式层已经字面为零；这不是跳过 53 个检查。完整 source/current 记录分别保其证据。

## 4. 38 维完整 self 像和全部基来源

定义

$$
\mathscr S_{53}:\mathbb Q^{53}\longrightarrow
 \mathbb Q[x,u,p,r],\qquad e_i\longmapsto F_i.
\tag{9}
$$

唯一实际给出

$$
\operatorname{rank}\mathscr S_{53}=38,\qquad
\dim\ker\mathscr S_{53}=15.
\tag{10}
$$

以下 38 个 **原列** $F_i$ 构成基。表中 pivot 是对应准确消元记录中的第一个新坐标，**并非声称整列只有该单项**。每个 pivot 记录同时给完整规范向量、其 53 列组合和展开到 144 原标签的 source。

所有序号均指同一次原 stdout 的 SELF_KERNEL_RECORD.sequence；第二列特指上节固定 R434 原 stdout 的 CURRENT_Q_RECORD.sequence。
| $i$ | R434 dependent 序号 | R443 来源 / 全 current / self pivot / union pivot 序号 | self 增量 pivot 单项 |
|---:|---:|---|---|
| 8 | 745 | 12 / 65 / 130 / 194 | $ur^{4}$ |
| 9 | 759 | 13 / 66 / 131 / 195 | $pr^{4}$ |
| 10 | 760 | 14 / 67 / 132 / 196 | $p^{2}r^{3}$ |
| 11 | 761 | 15 / 68 / 133 / 197 | $xpr^{4}$ |
| 12 | 762 | 16 / 69 / 134 / 198 | $p^{3}r^{2}$ |
| 13 | 763 | 17 / 70 / 135 / 199 | $upr^{3}$ |
| 15 | 768 | 19 / 72 / 137 / 201 | $xp^{2}r^{3}$ |
| 16 | 769 | 20 / 73 / 138 / 202 | $xur^{4}$ |
| 17 | 771 | 21 / 74 / 139 / 203 | $p^{4}r$ |
| 18 | 773 | 22 / 75 / 140 / 204 | $p^{5}$ |
| 20 | 776 | 24 / 77 / 142 / 206 | $x^{2}pr^{4}$ |
| 22 | 778 | 26 / 79 / 144 / 208 | $up^{2}r^{2}$ |
| 23 | 779 | 27 / 80 / 145 / 209 | $xp^{3}r^{2}$ |
| 25 | 784 | 29 / 82 / 147 / 211 | $xupr^{3}$ |
| 26 | 785 | 30 / 83 / 148 / 212 | $x^{2}p^{2}r^{3}$ |
| 27 | 787 | 31 / 84 / 149 / 213 | $up^{3}r$ |
| 28 | 791 | 32 / 85 / 150 / 214 | $x^{2}ur^{4}$ |
| 29 | 792 | 33 / 86 / 151 / 215 | $u^{2}pr^{2}$ |
| 30 | 793 | 34 / 87 / 152 / 216 | $xp^{4}r$ |
| 31 | 795 | 35 / 88 / 153 / 217 | $up^{4}$ |
| 33 | 799 | 37 / 90 / 155 / 219 | $x^{3}pr^{4}$ |
| 35 | 801 | 39 / 92 / 157 / 221 | $xup^{2}r^{2}$ |
| 36 | 802 | 40 / 93 / 158 / 222 | $x^{2}p^{3}r^{2}$ |
| 37 | 803 | 41 / 94 / 159 / 223 | $u^{2}p^{2}r$ |
| 38 | 804 | 42 / 95 / 160 / 224 | $u^{3}r^{2}$ |
| 40 | 807 | 44 / 97 / 162 / 226 | $x^{2}upr^{3}$ |
| 41 | 808 | 45 / 98 / 163 / 227 | $x^{3}ur^{4}$ |
| 42 | 809 | 46 / 99 / 164 / 228 | $xp^{5}$ |
| 43 | 810 | 47 / 100 / 165 / 229 | $xup^{3}r$ |
| 44 | 811 | 48 / 101 / 166 / 230 | $u^{2}p^{3}$ |
| 45 | 812 | 49 / 102 / 167 / 231 | $u^{3}pr$ |
| 46 | 814 | 50 / 103 / 168 / 232 | $x^{4}pr^{4}$ |
| 47 | 815 | 51 / 104 / 169 / 233 | $xu^{2}pr^{2}$ |
| 48 | 816 | 52 / 105 / 170 / 234 | $x^{2}up^{2}r^{2}$ |
| 49 | 817 | 53 / 106 / 171 / 235 | $xup^{4}$ |
| 50 | 818 | 54 / 107 / 172 / 236 | $x^{2}u^{2}pr^{2}$ |
| 51 | 819 | 55 / 108 / 173 / 237 | $u^{3}p^{2}$ |
| 52 | 820 | 56 / 109 / 174 / 238 | $xu^{2}p^{3}$ |

例如实际完整原列 $F_8$ 为

$$
F_8=-\frac59ur^4,
\qquad
V_8=-\frac5{18}B_RH_1+\frac59B_SH_1+
 \frac1{36}B_PH_2+B_PJ_0.
\tag{11}
$$

故其规范方向 $-\frac95V_8$ 准确给 $ur^4$；原记录 130/249 同时输出其完整 144 标签来源。这与 R441 的同方向是成员比较，不是重新计算旧结果。

### 4.1 完整 15 个输入核关系

前八条是

$$
F_0=F_1=\cdots=F_7=0.
\tag{12}
$$

它们依次来自 $B_PH_0,B_RH_0,B_SH_0,B_LH_0,B_UH_0,
B_VH_0,B_TH_0,B_YH_0$，原记录 122—129。其余七条准确为：
| 最后列 | 完整零关系 | 原记录序号 |
|---:|---|---:|
| 14 | $\frac{11}{2560}F_{8}+\frac{1}{2}F_{10}+\frac{1}{2}F_{11}+F_{14}=0$ | 136 |
| 19 | $\frac{1}{160}F_{8}+2F_{10}+F_{11}+F_{19}=0$ | 141 |
| 21 | $-\frac{942}{2627}F_{12}+\frac{2762}{2627}F_{13}-\frac{19}{2627}F_{15}-\frac{3605}{2627}F_{16}-\frac{38}{2627}F_{20}+F_{21}=0$ | 143 |
| 24 | $\frac{3786}{2627}F_{12}+\frac{2486}{2627}F_{13}+\frac{662}{2627}F_{15}+\frac{6976}{2627}F_{16}+\frac{1324}{2627}F_{20}+F_{24}=0$ | 146 |
| 32 | $-\frac{5376}{2627}F_{12}-\frac{35104}{2627}F_{13}+\frac{28136}{2627}F_{15}-\frac{60464}{2627}F_{16}-\frac{6776}{2627}F_{20}+F_{32}=0$ | 154 |
| 34 | $\frac{390856}{5973}F_{17}-\frac{482968}{5973}F_{22}-\frac{25696}{543}F_{23}-\frac{114922}{5973}F_{25}-\frac{299380}{5973}F_{26}-\frac{264290}{1991}F_{28}+\frac{3535}{11946}F_{33}+F_{34}=0$ | 156 |
| 39 | $\frac{69552}{1991}F_{17}-\frac{60120}{1991}F_{22}-\frac{3400}{181}F_{23}-\frac{11590}{1991}F_{25}-\frac{36420}{1991}F_{26}-\frac{84026}{1991}F_{28}-\frac{2091}{3982}F_{33}+F_{39}=0$ | 161 |

每条关系的最后列此前未作依赖，因此这 15 条在 53 维输入系数空间中独立；38 个准确 pivot 与 15 条完整零关系共同给出 (10)，没有以数值容差判秩。

这些零关系只说明相应的退化 self-current 恒零；不把它们误称为完整四阶成本恒零。

## 5. 与 K 链合并：完整 49 维，而非旧 22 维

[R435](R435-complete-local-self-currents-and-joint-actual-internal-flux-control.md) 已付的 K 链用原完整生成式编码。令

$$
w=1-zx,\qquad A_z=w^2r+2zwp+2z^2u.
$$

在 $\mathcal A=0$ 处，

$$
\mathfrak F_z=
\frac{A_z^3}{15}
 \left(4A_z^2-10z^2uA_z-\frac{20}{3}w^4r^2\right),
\qquad
K_n\ \mapsto\ n![z^n]\mathfrak F_z,\quad 0\le n\le10.
\tag{13}
$$

本次只消费这个已付完整式，未重新证明旧 11 列独立，也没有把 $[z^n]$ 漏掉 $n!$。

构造一次真正的新 union 映射

$$
\mathscr S_{64}:
 (\lambda_0,\ldots,\lambda_{10},c_0,\ldots,c_{52})
 \longmapsto
 \sum_{n=0}^{10}\lambda_n\,\mathfrak S(K_n)
 +\sum_{i=0}^{52}c_iF_i.
\tag{14}
$$

其准确结果为

$$
\operatorname{rank}\mathscr S_{64}=49,\qquad
\dim\ker\mathscr S_{64}=15.
\tag{15}
$$

一组完整基就是 **全部 11 个 K 列，加第 4 节的全部 38 个 $F_i$**。原 union 记录 175—185 给 K 的基证书；第 4 节最后一个序号给各原 $F_i$ 在同一 union 消元中的基证书。union kernel 的 15 条仍由第 4.1 节原关系生成，未出现 K 与 38 维 self 像之间的新依赖。

因此这里是两个明确模块的直和像结论，而不是从两个单独 rank 相加作猜测。

### 5.1 原 22 方向的完整成员证书

原 22 方向为 K 的 11 列，加以下 11 个非 K 方向。每个比较记录均输出准确组合、完整原标签 source，以及空的 full_current_residual：
| 旧 current | 新 53 列的准确表示 | 原记录序号 |
|---|---|---:|
| `J_sigma` | $-\frac{3}{80}F_{8}-16F_{10}+16F_{11}$ | 239 |
| `J_1` | $-128F_{9}$ | 240 |
| `J_2` | $-\frac{3}{10}F_{8}-128F_{10}-128F_{11}$ | 241 |
| `J_3` | $\frac{484608}{2627}F_{12}+\frac{318208}{2627}F_{13}+\frac{84736}{2627}F_{15}+\frac{892928}{2627}F_{16}+\frac{169472}{2627}F_{20}$ | 242 |
| `W_sigma` | $\frac{30144}{2627}F_{12}-\frac{88384}{2627}F_{13}+\frac{608}{2627}F_{15}-\frac{136832}{2627}F_{16}+\frac{1216}{2627}F_{20}$ | 243 |
| `W_2` | $256F_{16}$ | 244 |
| `W_3` | $-128F_{26}$ | 245 |
| `Xi_0` | $-512F_{12}+256F_{15}$ | 246 |
| `Xi_1` | $256F_{17}$ | 247 |
| `Xi_2` | $256F_{18}$ | 248 |
| `U_star` | $-\frac{9}{5}F_{8}$ | 249 |

因此原 22 维模块准确包含在 (15) 内，而且

$$
49-22=27
\tag{16}
$$

个新增形式方向确实存在。旧 22 维仅作为已发表结果和此次 union 的输入，没有再次执行它的独立 rank 任务。

## 6. 哪些实际条件保持，哪些尚未支付

53 个 $V_i$ 的 whole-Q 和三尾 Af-current 零关系来自 R434 原证书；其 third-diagonal 核来源给原 pure 零。原响应空间的 universal natural 流零按 [R344](R344-general-pure-factorization-of-total-response-flux-with-ordered-Green-tails.md)、[R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md) 使用。因此这些是保相应 whole-E、共同有限 natural 读出及 ordered Af 通道的**准确有号响应方向**。K 链的相应保持范围沿 R435。

本次新增的是它们的完整 self-current 像。它为同一最终 profile 库上的 self/Hd 调节提供了比旧 22 维更大的候选模块，但以下步骤没有在本次完成：

- 将 (15) 评价到同一实际母库的全部简单 Af 根；
- 在共同镜点固定 $s=p_*/r_*$、$h=u_*/r_*$ 后求准确像及余核；
- 把该实际评价像与一般 canonical 成本的真实 self 目标逐一比较；
- 追加这些查询后，重做同一原型基准和同一合法窗口下所需的实际联合截面；
- 支付原全部内部通量、平台仿射闭合、两个 period 特解和 13 行同规范系统。

特别地，旧“16 个实际镜对值加 6 个 blind 方向”的描述仍是其原 22 维子模块的准确结论，但**不是**增广 49 维模块的完整判据。也没有理由把形式 rank 49 写成实际 rank 49。

另一项关键区分：第 4.1 节的核是退化点 self-current 核，不等于全点函数 $2K_{\tau,u}(q_E)$ 为零；(5) 代入前仍完整保存原 primitive。

## 7. 唯一执行、计费与规则读入

### 7.1 唯一新执行及分阶段成本

新 request 的范围为 53 个 self 列、11 个已付 K 编码、11 个旧非 K 参考的成员比较；两个新 adapter 是仅有的开发检查。实际所有阶段均完成：

| 阶段 | 实际 seconds | 完成内容 |
|---|---:|---|
| 读取并绑定已付原输入 | 1.8003764800000113 | 原 run/job/source/status、原 log/request、原 1020 记录身份 |
| 新开发检查 | 0.00515094700000418 | 2 个 adapter |
| 新 source 组合 | 0.03926271200000997 | 53 条关系展开到 144 标签 |
| 完整 53 self-current | 1.1481041239999854 | 全 current、Af、Green 和残余分类 |
| 新 self/union/成员比较 | 0.10423999599998979 | 53 self、64 union、11 MEMBER |
| 全部 science | 1.2916408000000104 | 上述三个 science 阶段 |
| entry 到最终 report 冻结前 | 3.149657480000002 | 全入口 |
| entry 含最后 summary 序列化 | 3.15011495600001 | 最终完整时间 |

峰值 RSS 为 **45,356 KiB**。science 的受监控有理运算 56,706 次，最大有理位数 50；新 primitive 调用 421、cache 1,710、profile atoms 300，全部无 overshoot。开发阶段为 234 次受监控有理运算、最大位数 3、primitive 11、cache 47。

受监控运算口径仅为进入 Limits.rational 的调用，不冒充继承表达式内部所有算术的全计数。

预定上限为 science 180 秒、开发 20 秒、内存 1024 MiB、数学 stdout 2,500,000 bytes、词调用 500,000、共享 cache 300,000、受监控有理运算 5,000,000。本次没有超限、失败后续跑或第二次 science。

原 18 构造、原 Q/current 映射、原 Q/current rank、旧检查的执行数均为 **0**；实际 profile/根评价数也为 **0**。

### 7.2 真实 pull、同一 source 与窗口边界

workflow 先读取原规则并作实际 public/private pull，随后 detached 回固定 source，才运行上述两个 adapter 和 science。

- public pull：04:03:21.386494Z 至 04:03:21.810891Z；before/after 均为 9c796878a2f7f1b910ebcebadd0b2d05dc0d42ac；return code 0，两 README diff 为空。
- public 根 README blob：21bd547f56590b7f2dd279d0297efb289a9b2783；topic README：d0432faff569c8e9af7ed4809847e12880976c11。
- private pull：04:03:24.300237Z 至 04:03:26.208276Z；7bc383cea1827ba24527d7b0c309816a8477c5ac 到 bb3e517201132c8cb2ef26c8f0fec7639332893c。
- private 根 README blob：5ba164843b1f5802184178a82d786264404873a3；topic README 不存在；两次读值一致，QUEUE 当前会话 unique/ongoing 为真。没有输出私有正文。
- detached source 精确为上列 9c796878…；11 个 source binding 全部核对。

这些是该次实际运行的规则与来源记录，不为本稿新增任何实际几何窗口、profile、成本或 period 结论。

## 8. 全记录索引和字节身份

原 stdout 的 249 个 SELF_KERNEL_RECORD 包含：

| kind | 条数 | sequence |
|---|---:|---|
| input.paid_original_output_identity | 1 | 1 |
| development.new_adapter_check | 2 | 2—3 |
| science.paid_relation_new_self_source | 53 | 4—56 |
| science.complete_self_column | 53 | 57—109 |
| science.new_self_coordinate_labels | 1 | 110 |
| science.paid_K_reference_encoding | 11 | 111—121 |
| science.new_self_image_step | 53 | 122—174 |
| science.new_K_plus_paid_kernel_self_image_step | 64 | 175—238 |
| science.published_reference_in_new_self_image | 11 | 239—249 |

每个 envelope 均含 sequence、kind、payload_bytes、payload_sha256 和完整 payload。第 4 节的来源表给全部 38 个基逐项定位；(12) 与第 4.1 节给全部 15 个输入核，成员表给全部旧非 K 方向。K 的完整生成式由 (13) 给出。

人类回读只从这一条已完成 stdout 解码，逐项对上 **249 个 payload 字节数/SHA、JSONL 总 SHA、身份链和最终报告 SHA**，没有重做数学消元或另取一次 log。

| 对象 | bytes | SHA256 |
|---|---:|---|
| 原完整 job stdout | 421,834 | d4a266bb80006a56918f21600ecce75ade0b7522ddbfc45459f89958f5b2c1e8 |
| 249-record JSONL | 299,732 | 1ea691a9cb902e6be7bdbf09b892c3f39d665dbd45174a309be7445686611ca8 |
| record identity chain | 41,391 字节 canonical identity 输入 | 6565a3135f586abdbeda18ae58dae8b156e820d81e1f448e1afa0f5339a190c5 |
| COMPLETE_REPORT JSON 加 LF | 17,727 | 070de2b03125ef6a3be251919dc99ecc736b47a00261708cea0727e5c7d36dc4 |
| 本次 request | 11,809 | f3523f5ee89d820150e52e22c54afd25d5d7deb79fa8adc0d5cbefc7496f4532 |

数学记录 stdout 为 304,463 bytes，completed-but-not-emitted 列表为空，249 条全部发出。最终 COMPLETE_REPORT 的 entry_outcome 为 complete_new_observation，science outcome 为 complete_new_self_image_with_additional_formal_directions，exit code 为 0。

原机器 payload 没有提交、上传、另建 blob 或 artifact；本稿只写人类定理、准确证书索引及来源。runner 临时 JSON/JSONL 的名称仅是该次输出记录，不另造一份科学结果。

## 9. 固定源码清单

本次四个新文件为 workflow、design、driver、request；其余为原纯接口或规则 reader。全部以同一个 source commit 读入：
| source 文件 | bytes | SHA256 |
|---|---:|---|
| `.github/workflows/visible-joint-kernel-complete-self.yml` | 5267 | `d04a544f9d21bc8d0a053cc44a82ee27ebb462aacfd150c9265f24cebfdc613f` |
| `topics/visible-flex-new-mechanism/notes/joint-kernel-complete-self-design-20261116.md` | 13644 | `b1d8ff3a93cba71176641589011c5578d74172f8267a15356b447c2935fd84af` |
| `topics/visible-flex-new-mechanism/scripts/literature_color_priority_words.py` | 21642 | `ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9` |
| `topics/visible-flex-new-mechanism/scripts/literature_colored_profile_algebra.py` | 15738 | `c0d87a214f27a03fb29cd07cc5e9740249580da7f854ed4ff02d6eaf69b1f66f` |
| `topics/visible-flex-new-mechanism/scripts/literature_complete_response_self_current.py` | 54281 | `18d5578869860f9da52d31137352f6a503a27610eab5e133b9a1c0f9ca85e8f5` |
| `topics/visible-flex-new-mechanism/scripts/literature_full_self_euler_coordinates.py` | 10966 | `95ec818ce1fdf815b0390aaf2ad4f976a0dfc7bd0b5218899acd4f4bc271f9ba` |
| `topics/visible-flex-new-mechanism/scripts/literature_joint_kernel_complete_self.py` | 42222 | `f651b7c89c4ed7ff08c8b0b18d903846a95b520fd28d3d504cf22bf36410f11e` |
| `topics/visible-flex-new-mechanism/scripts/literature_pure_bulk_exact_membership.py` | 33718 | `f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70` |
| `topics/visible-flex-new-mechanism/scripts/literature_pure_bulk_word_normal_form.py` | 32310 | `d39482c9e33e7358f1afa51b073daf5f65e84b4858f9a18f446206e8f9d9ea65` |
| `topics/visible-flex-new-mechanism/scripts/literature_range_profile_algebra.py` | 33169 | `a7f1771a33a8e73934f9549b3407a9e351fed59a9eec163c5b11c965c7f1dc52` |
| `topics/visible-flex-new-mechanism/scripts/read_original_actions_log.py` | 50679 | `b7b16d0917bf99e4183421ab6d5c1dd33b9c0fe8009ad59a5141a17d798e5c4a` |

request 路径为 computations/request-joint-kernel-complete-self.json（相对本 topic），其 identity 已列第 8 节。设计为 [joint-kernel-complete-self-design-20261116.md](../notes/joint-kernel-complete-self-design-20261116.md)，新 driver 为 [literature_joint_kernel_complete_self.py](../scripts/literature_joint_kernel_complete_self.py)。

本次 driver 只调用原库的表达式、精确坐标及同锚纯接口；没有调用旧 original_operators、map_Q、current_record、development、science 或 main 的旧研究任务。源码中的 LIMITS 与新 request 的共同界限一致。

## 10. 此次完成后的准确研究状态

本次解决了一个完整问题：**原 144 响应的已付 whole-Q / 三尾 current 联合核，其全部 53 条准确关系在 Af 上的 self 像为 38 维；加 K 链后为 49 维。** 所有局部性残余都已在这次完整计算中消失，全部 11 个旧非 K 方向确切包含，旧 22 维不是本模块的终点。

下一真实问题是把这 49 个完整函数，在同一个已构造母库、同一个实际宽度/中心和全部真实 Af 根上评价，保每个响应的完整 source 与原 joint 基准，判断其实际像外商。该任务不能用自由 jet 秩代替；当前稿也不把它包装成已经付清的完整 period 或同一 gauge 解。
