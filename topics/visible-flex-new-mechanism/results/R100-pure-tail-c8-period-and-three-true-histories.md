# R100：D25 的 $c^8$ 周期系数与三个真实零端历史

日期：2026-11-14。**已证明，且已有公开准确回代证书。** 只讨论单位幂尾 $q=(c-\xi)^8$ 的 D25 系数，不把本结果推广到所有尾指数。这里 D25 是完整第四 period 密度中 $(c-\xi)^{25}$ 的系数；$c$ 是尾端点参数。保留真实 $s$ 历史，从同一个零初值恢复。

假设 $h>0$、$h,k,\omega$ 为真实光滑有限路径，满足 $\omega_s=k_s/(2h)$，首末为常 scalar 芽，且完整第二矩阵 $M=0$。本稿证明：D25 period 的 $c^8$ 系数等于式 (19) 的三个真实零端历史 action；式 (17) 是被准确支付的完整端势。证明不要求第三算子 $T=0$，也没有证明 action 的符号、非零周期、零成本环或完整第四 range。

[R95](R95-compressed-D25-action-and-top-parameter-endpoint-potentials.md) 已支付完整压缩及 $c^{10},c^9$ 两端势。本稿逐步给出下一项；公开 run `43640085842` 的独立 consumer 已从已发布完整原 DAG 验证全部身份，没有重编 forcing 或评价一条实际几何路径。

## 1. 输入、归一化与真实参数系数

在固定端点参数 $c$ 下定义

$$
z=c+\omega,\qquad e=hz-k,\qquad Q=1+e^2,
$$

$$
K=kz^2-\frac{k^2+1}{h}z-\partial_s^2(z/h),\qquad
C=KQ/(8h),\quad D=Ke/4,\quad f=Q/(8h^2).
$$

全部 $s$ 导数固定 $c$。沿用 R95 的

$$
\begin{aligned}
\mathcal A={}&L_0+b\widetilde L_b
+\frac{169}{480}b^2\left(C_{cc}-5D_c+\frac{17}{20}hK\right)\\
&+b(C_c+2D)\left(\frac{217217}{1350}J-\frac{8281}{43200}d\right).
\end{aligned}
\tag{1}
$$

这里 $\mathcal A$ 已经只差准确零端势而代表原 D25 period，$A=3136/13$，$B=b/A$。真实 ODE 给

$$
B_s=C,\quad J_s=D,\quad d=xB_c+yJ,
\qquad x=-2304/13,\quad y=-608/13.
\tag{2}
$$

令

$$
C=\sum_{j=0}^4 C_jc^j,\quad D=\sum_{j=0}^3D_jc^j,
\quad B=\sum_{j=0}^4B_jc^j,\quad J=\sum_{j=0}^3J_jc^j.
$$

每个系数 primitive 都有真实定义

$$
B_j'=C_j,\quad J_j'=D_j,\qquad B_j(0)=J_j(0)=0.
\tag{3}
$$

完整 $M=0$ 给其全部末值也为零。$D_3=2C_4$ 还给 $J_3=2B_4$。参数多项式身份通过 (2)、(3) 的 ODE 和初值唯一性建立；没有在区间内部把 history 置零。

下文用

$$
p=B_4,\quad \eta=\omega-k/h,\quad
G=k^2-1+h\ell_h,\quad \ell_h=(h_s/h^2)_s,
\qquad \mathfrak m=\frac{169A^2}{480}=\frac{307328}{15}.
\tag{4}
$$

特别 $p'=C_4=hk/8$。

## 2. 移动参数下的局部恒等式

由唯一真实关系 $\omega_s=k_s/(2h)$，

$$
\eta_s=\frac{k h_s}{h^2}-\frac{k_s}{2h}.
$$

置 $v=c+\eta$，则 $z=v+k/h$，且

$$
\lambda=\frac{h_s}{h^2}v+\frac{\eta_s}{h},\qquad
hK=hk\,v^2+Gv+\eta_{ss}-k/h.
\tag{5}
$$

第二式中 $\lambda_s$ 的两个交叉项准确抵消。于是

$$
\begin{aligned}
C_3&=4\eta p'+G/8,&D_2&=6\eta p'+G/4,\\
C_2&=6\eta^2p'+3\eta G/8+\eta_{ss}/8,
&D_1&=6\eta^2p'+\eta G/2+\eta_{ss}/4-k/(4h).
\end{aligned}
\tag{6}
$$

这些式子保留真实 $h,k,\omega$ 的全部相关性。

## 3. 两个局部小系数

公开原始系数表的 $[c^8]L_0$ 只有四项：

$$
[c^8]L_0
=\frac{2401}{75}\frac{h_s^2k}{h}
-\frac{16807}{150}hk-\frac{2401}{150}hk^3
-\frac{2401}{150}h_{ss}k
=-\frac{2401}{150}hk(G+8).
\tag{7}
$$

将 R95 已证的 $f_s\{\gamma_JD+\gamma_d(xC_c+yD)\}$ 从原 $L_b$ 扣除，最高系数为

$$
[c^4]\widetilde L_b
=-\frac{1911}{400}k\left(k_s-\frac{2kh_s}{h}\right).
\tag{8}
$$

新 consumer 分别核 (7)、(8)，不会仅从主报告中的总项数推断。因为 $b=A B$，这两个局部项对 $[c^8]\mathcal A/\mathfrak m$ 的贡献恰为

$$
-\frac{p'(G+8)}{160}+\frac9{10}pp'\eta_s.
\tag{9}
$$

## 4. 先消去 $B_2,J_1$ 的最高入口

R95 的二次部分除以 $\mathfrak m$ 为

$$
B^2\left(C_{cc}-5D_c+\frac{17}{20}hK\right)
+\frac25B(B_c+5J)(C_c+2D).
\tag{10}
$$

直接取 $c^8$ 系数，再减去

$$
D_s\Phi_{8,0},\qquad
\Phi_{8,0}=\frac{72}{5}p^2B_2+8p^2J_1
-\frac85pB_3^2+16pB_3J_2,
\tag{11}
$$

剩余二次部分为

$$
p^2\left(-\frac65C_2-\frac95D_1+\frac{17}{20}[c^0](hK)\right)
+\frac25p(11B_3-5J_2)(5C_3-2D_2).
\tag{12}
$$

例如 (11) 中四项分别支付 $pp'B_2$、$pp'J_1$、$p'B_3^2$、$p'B_3J_2$；微分产生的全部其他项正是 (12) 中保留的系数。

定义真实辅助组合

$$
v_0=2J_2-3B_3,\qquad w=B_3-J_2/2.
$$

由 (6)，

$$
v_0'=G/8,\qquad w'=\eta p',\qquad
11B_3-5J_2=14w+v_0,\quad 5C_3-2D_2=8\eta p'+v_0'.
\tag{13}
$$

另置 $S=13B_2-6J_1$，(6) 给

$$
S'=42\eta^2p'+15\eta v_0'+\eta_{ss}/8+3k/(2h).
$$

等价地，(12) 中的局部括号为

$$
-\frac65C_2-\frac95D_1+\frac{17}{20}[c^0](hK)
=-\frac{56}{5}\eta^2p'-4\eta v_0'+\frac14\eta_{ss}-\frac25k/h.
\tag{14}
$$

## 5. 完整端势和短 action

定义三个实际历史坐标

$$
\ell=w-\eta p=B_3-J_2/2-\eta p,
\qquad \zeta=v_0+4\ell=B_3-4\eta p.
$$

其真实方程及边界为

$$
p'=hk/8,\quad \ell'=-\eta_s p,\quad
\zeta'=G/8-4\eta_s p,
\qquad (p,\ell,\zeta)(0)=(p,\ell,\zeta)(L)=0.
\tag{15}
$$

它们由原 $B_j,J_j$ 唯一确定，不是可独立指定的控制。

将 (9)、(12)–(14) 合并，并逐次分部，得到完整恒等式

$$
\boxed{\quad
[c^8]\mathcal A
=\mathfrak m\{D_s\Phi_8+\mathcal R_8\},\quad}
\tag{16}
$$

其中

$$
\begin{aligned}
\Phi_8={}&\frac{72}{5}p^2B_2+8p^2J_1-\frac85pB_3^2+16pB_3J_2\\
&-\frac{56}{5}\eta^2p^3
+\frac85\eta p^2(11B_3-5J_2)
+\frac14p^2\eta_s-\frac1{20}p,
\end{aligned}
\tag{17}
$$

$$
\boxed{\quad
\mathcal R_8
=\frac25p(\zeta+10\ell)\zeta'
-\frac25\frac kh p^2
-\frac1{20}p'\zeta'-\frac15p'\ell'.\quad}
\tag{18}
$$

为核对分部的符号，在 (11) 后先加入

$$
\frac{56}{5}\eta^2p^3
+\frac85\eta p^2(14\ell+v_0)
+\frac14p^2\eta_s-\frac1{20}p.
$$

用 $14\ell+v_0=11B_3-5J_2-14\eta p$ 就得到 (17) 后一行。前两项的导数把含 $\eta p'$、$\eta v_0'$ 的部分合成为

$$
\frac25p(14\ell+v_0)(v_0'+4\ell')
=\frac25p(\zeta+10\ell)\zeta'.
$$

$p^2\eta_s/4$ 的导数保留 $-p'\ell'/5$ 与 $-p'\zeta'/20$，而 $-p/20$ 支付 (9) 中的剩余 $-p'/20$。因此没有遗漏原式中的局部常数项。

所有 (17) 的项都含 $p$，所以 $p(0)=p(L)=0$ 已足支付端势。完整 $M=0$ 下

$$
[c^8]\int_0^L D25\,ds
=\mathfrak m\int_0^L\mathcal R_8\,ds.
\tag{19}
$$

这一约简不要求另假设 $T=0$；需要研究真正 $M=T=0$ 环时，可在相应子类使用它。它仍没有判定右边的符号或非零。

## 6. R97 完全平方在这些坐标中的准确位置

设 $\rho=h_s/h$、$u=8p/h=F/h$。由 (15) 和真实 $\eta_s$ 得

$$
(8\ell-uk/2)'=-\frac12k(k+u\rho),
\tag{20}
$$

$$
(8\zeta-\rho-2uk)'
=(u^2-1)\rho^2-(k+u\rho)^2-1.
\tag{21}
$$

常 scalar 端芽下 $\rho$ 两端为零，且 $u,\ell,\zeta$ 两端为零。(20)、(21) 积分正好给 [R97](R97-zero-matrix-paths-require-nonconstant-h.md) 的相关式及完全平方式。

因此 R97 的信息已在短 action 的真实边界条件中出现。不能把 (20)、(21) 的右边逐点设为零，也不能因 (21) 有平方而直接给 (18) 授正性：后者的权含 $p,\ell,\zeta$，没有在此证明固定符号。

作为范围核对，真实倒行保持 $h,k,\eta$ 的反向取值，而完整零矩阵下 $p,\ell,\zeta$ 反号、其导数不反号，所以 (18) 是倒行偶的。这与 R83 的 $V_{\mathrm{rev}}=V$ 一致，并不提供负成本环。

## 7. 公开实际证书与可复核范围

唯一研究运算在本公开仓库 Actions 执行。run `43640085842`、source `bccbbe27c8c105666b2d2438b9d1d48812e3ce55`，lane `pure_tail_c8_reduce` 已成功，完成用时 11.634193078 秒，峰值 RSS 96.859375 MiB。

[主报告](../notes/actions-43640085842-1-pure_tail_c8_reduce/pure-tail-c8-action.json)、[完整证书](../notes/actions-43640085842-1-pure_tail_c8_reduce/pure-tail-c8-action-certificate.json.gz)和[可读短式](../notes/actions-43640085842-1-pure_tail_c8_reduce/pure-tail-c8-action-expressions.json)均已公开。源码是独立的 [literature_pure_tail_c8_reduce.py](../scripts/literature_pure_tail_c8_reduce.py)，SHA256 为 `1f4dfb341ee76e5cb2cbc9ca9b36f0153838572a5e354d1c64bed27ce49bad0d`；没有修改已发布 R56、R92、R95 的计算源。

consumer 保留输入的 18 个真实 history，增加 $B_0,B_1,B_2,J_0,J_1$ 五条真实零初值 ODE。原有 $B_4,B_3,J_2$ 继续使用，$J_3=2B_4$ 单独核同 ODE。因此共有 23 个真实 history；原作用中的 $b(c),d(c),J(c)$ 均由同 ODE、同初值唯一性重建，没有将形式状态逐个设零。

准确核验包含：

- 九个 $B_j,J_j$ 系数 ODE、原三个 history 的 ODE/零初值、完整参数族的 ODE/零初值与 fresh 回代；
- 移动参数式 (5)、两个局部小系数 (7)、(8)、真实 $\ell,\zeta$ ODE；
- 完整端势加短 action 的式 (16)，以及仅令 $B_4=0$ 即得端势为零；
- 原始 D25 DAG 输入身份、fresh 参数族 $c^8$ 身份；
- R97 的两个真正 primitive 导数式 (20)、(21)，并保留其零端积分含义。

全部 34 条准确差式均为零，所有差式的规范化项数均为 0。未出现预期外的遗留 history。规范化 $c^8$ 原式有 31 项；用真实导数展开短式后有 19 项、七个 history 单项式组。这些非零形式项数不证明真实周期非零；它们仍须沿同时满足真实 ODE 与端条件的路径积分。

完整证书 gzip 为 78,737 字节，SHA256
`60761416a641f702d60d161fcad1f161c406d6e3969c76f25e090d256a89dab3`；解压后的 699,591 字节 SHA256 为
`4b2fdc4d5210094575a14316a63705bb392d322aba862731d33727e79928f2df`。
可读表达式 4,792 字节，SHA256 为
`4804f668347514f545a0ce683c65cc9c6bb669d3fdf034c26de5cf3fb361e94c`。

原人工开发仅核制造的多项式路径及故意错误系数，未执行研究目标。上述完整回代由本次公开 Actions 支付。报告明确 `action_sign_proved=false`、`nonzero_period_proved=false`、`new_zero_cost_loop_proved=false`。

## 8. 下一问题的准确位置

本结果把下一阶问题缩为 (18) 的真实路径积分。R97 约束已包含于 (20)、(21) 及其边界；不能再把三个 history 当独立测试变量，也不能把平方恒等式的 integrand 逐点设零。即使对某条 $M=0$ 路径得到非零积分，讨论 R83 的第四成本半群时仍须另支付所需 $T=0$、共同 profile 与共同物理区间。

符号翻转、左右 collar 交换或幂尾端点变换必须同时追踪完整恢复式的锚。它们不能仅凭 (18) 的形式反号产生一个真实负第四成本环。当前结果为继续判断完整 $P_0$ 提供已核的短式，没有预判其可控性或正性。
