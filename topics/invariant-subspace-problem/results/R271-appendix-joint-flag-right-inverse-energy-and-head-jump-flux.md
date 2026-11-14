# R271 后续附录：联合旗链的预算内右逆、严格正能量与有限头跃迁通量

日期：2026-11-13（UTC）。作者：boundary_resume_1cf / Astra-ISP-1cf8c51d；主会话完成实际域、链符号及逐项预算复核。状态：以下受限满射、正能量及通量公式已证明；尚未排除真正缺陷。

本稿继续[残量及全部可行链的联合旗](R271-appendix-orthogonal-residual-flags-and-exact-source-gram.md)和 [R239 闭链/末端泄漏](../results/R239-appendix-closed-repair-chain-riccati-and-terminal-leakage.md)。旧全源链的固定 $q$ 闭像常数未必在实际进位预算内。这里利用全部逐头删除核，把受限链的右逆代价降到 $e^{d^4}$ 以内；真实进位和投影误差乘最优对偶范数后均可吸收。剩余通量转为原有限头跨越至少两格的真实跃迁，不将它误称为小进位。

固定 $m,q$ 的联合旗闭像/对偶极小值取得亦已由 [R239 有限尾塔推论](../notes/2026-11-13-finite-tail-tower-corollary-for-exact-residual-flags-boundary-resume.md)补全。本稿不重计该定性结论；新增的是准确受限输出上的同时右逆、$e^{d^4}$ 成本、进位吸收以及真实有限头跃迁通量。

## 1. 联合旗和它的准确输出空间

保持原线性物理位号：
$$
 m\ge5,\quad d=2^m,\quad
 4d\le q\le e^{d^3/4},\quad
 A=A_m,\quad D=D_m,\quad L=A+D.
$$
原头标准正交基为 $e_0,\ldots,e_{d-1}$，且
$$
 W_k=\operatorname{span}(e_0,\ldots,e_{k-1}),
 \quad \ker A^k=W_k,\quad
 (A^k)_{ij}=0\quad(j<i+k),\quad \|A\|\le6.
$$
记 $E_{h,p}=\ker D^h\cap\mathcal H_p^{\rm tail}$，约定 $E_{0,p}=0$。

已证的准确顶部残量范围与修复域是
$$
 \mathscr R=\bigoplus_{i=0}^{d-2}e_i\otimes E_{d-i-1,q},
$$
$$
 \mathscr C_{\rm flag}
 =\bigoplus_{t=1}^d\mathscr C_t,\qquad
 \mathscr C_t=\bigoplus_{i=0}^{d-t}e_i\otimes E_{d-i,q+t}.
 \tag{1.1}
$$
定义
$$
 \mathscr Y_0=\mathscr R,\qquad
 \mathscr Y_s=
 \bigoplus_{j=0}^{d-s-1}e_j\otimes E_{d-j-1,q+s}
 \quad(1\le s\le d-1).
 \tag{1.2}
$$
这些都是原 Hilbert 度量下的闭正交直和。

内部输出
$$
 S_{\rm flag}c=(Ac_1+Dc_2,\ldots,Ac_{d-1}+Dc_d)
$$
准确取值于 $\bigoplus_{s=1}^{d-1}\mathscr Y_s$；末端 $Ac_d=0$ 已由
$\mathscr C_d=e_0\otimes E_{d,q+d}$ 自动满足。确实，$D$ 把核阶降低一，$A$ 的第 $i$ 行只使用 $j\ge i+1$，后者的核阶 $d-j\le d-i-1$。头位置也满足 (1.2)。

令
$$
 \mathcal Bc=(Dc_1,S_{\rm flag}c):
 \mathscr C_{\rm flag}\longrightarrow
 \bigoplus_{s=0}^{d-1}\mathscr Y_s.
 \tag{1.3}
$$

## 2. 同时解全部内部方程的相容右逆

使用同一个 R254J 相容族 $R_t$，输入上界取 $q+d$，最大原像阶取
$d$。可统一放大常数为
$$
 R=512\sqrt{q+2d+1}\,(m+q+2d+3)^{3/2}.
 \tag{2.1}
$$
它覆盖原 $(j+1)^{-2}$ 权；放大一个整数位置只增加余量。
相容性和受限界为
$$
 DR_t=R_{t-1},\quad R_0=I,\qquad
 \|R_tu\|\le(2R)^{h+t-1}\|u\|\quad(u\in E_{h,p}).
 \tag{2.2}
$$
所有输入层均在已声明有限范围内。

对 $f=(f_0,\ldots,f_{d-1})$，$f_s\in\mathscr Y_s$，定义
$$
 \boxed{
 (\mathcal Q f)_t
 =\sum_{s=0}^{t-1}(-A)^{t-s-1}R_{t-s}f_s
 \quad(1\le t\le d).
 }
 \tag{2.3}
$$
令 $k=t-s-1$。若输入头坐标为 $j$，则
$f_{s,j}\in E_{d-j-1,q+s}$。$R_{k+1}$ 将其核阶提高到
$d-j+k$，而 $A^k$ 只可能送往 $i\le j-k$。因此最终核阶至多
$d-i$。同时 $j\le d-s-1$ 给 $i\le d-t$，所以每项确在
$\mathscr C_t$。

直接使用 $DR_t=R_{t-1}$ 作有限望远镜：
$$
 D(\mathcal Qf)_1=f_0,\qquad
 A(\mathcal Qf)_t+D(\mathcal Qf)_{t+1}=f_t.
$$
无需交换 $D$ 与 $R_t$，亦无需把不同源层的右逆重新选择。因此
$$
 \boxed{\mathcal B\mathcal Q=I.}
 \tag{2.4}
$$

## 3. 关键阶数只支付 d−1，而非全源孔数 q

在 (2.3) 中，$A^k$ 杀去所有 $j<k$ 的头坐标。对其余 $j\ge k$，
(2.2) 的指数满足
$$
 (d-j-1)+(k+1)-1=d-j+k-1\le d-1.
$$
先在原正交头坐标分别用此界，再施加 $A^k$，得
$$
 \|A^kR_{k+1}f_s\|
 \le6^k(2R)^{d-1}\|f_s\|.
 \tag{3.1}
$$
对固定 $k$，从 $s$ 到 $t=s+k+1$ 只是正交直和坐标的移位，所以其整列算子范数也满足同一界。对 $k=0,\ldots,d-1$ 求和得到
$$
 \boxed{
 \|\mathcal Q\|\le C:=6^d(2R)^{d-1}.
 }
 \tag{3.2}
$$

合法窗中 $m\le d/2$、$q\ge4d$ 使 (2.1) 两个括号都小于
$2q$，故 $R\le2048q^2$。于是
$$
 \begin{aligned}
 \log C
 &\le d\log6+(d-1)(\log4096+2\log q)\\
 &\le \tfrac12d^4+11d\le d^4.
 \end{aligned}
$$
因此
$$
 \boxed{\|\mathcal Q\|\le C\le e^{d^4}.}
 \tag{3.3}
$$
这里控制的是完整源 $\mathscr R$ 和全部受限内部输出的同时右逆，不仅是某个给定残量。

把 $f_0=0$ 给 $S_{\rm flag}$ 的右逆，成本至多 $C$，且其第一段
$c_1=0$。把 $f_s=0\ (s\ge1)$ 给
$$
 F_{\rm flag}:\ker S_{\rm flag}\to\mathscr R,\qquad F_{\rm flag}c=Dc_1
$$
的右逆，成本也至多 $C$。

## 4. 可预算的准确正 Gram 与对偶极小值

$S_{\rm flag}$ 对 (1.2) 的内部输出空间满射，故其伴随单射、像闭且下界至少 $C^{-1}$。特别，联合旗稿的对偶 inf 现在取得，且在这个受限输出空间中的极小链唯一。

对 $y\in\mathscr R$，令
$$
 b_y=P_{\mathscr C_{\rm flag}}D_0^*y,\qquad
 z_y\in\bigoplus_{t=1}^{d-1}\mathscr Y_t,
$$
$$
 S_{\rm flag}^*z_y
 =P_{\operatorname{Ran}S_{\rm flag}^*}b_y,\qquad
 f_y=b_y-S_{\rm flag}^*z_y.
 \tag{4.1}
$$
于是
$$
 f_y=P_{\ker S_{\rm flag}}D_0^*y,\qquad
 \|z_y\|\le C\|b_y\|\le C\|y\|.
 \tag{4.2}
$$
准确旗 Gram 满足
$$
 \boxed{
 G_{\rm flag}=F_{\rm flag}F_{\rm flag}^*\ge C^{-2}I_{\mathscr R}
 \ge e^{-2d^4}I_{\mathscr R}.
 }
 \tag{4.3}
$$
这是实际 Schur 补的下界，不是环境创建下界。

对任何真实特殊源 $r\in\mathscr R$，取
$y=G_{\rm flag}^{-1}r$，并写原最小能量为 $\lambda=\lambda(r)$。
则
$$
 \boxed{
 f_y=c^{\min},\quad
 \langle r,y\rangle=\|f_y\|^2=\lambda^2,\quad
 \|y\|\le C\lambda,\quad
 \|z_y\|\le C^2\lambda.
 }
 \tag{4.4}
$$
因此原真实小误差乘这些对偶范数后仍在预算内；不再把这个问题留给未经控制的全源闭像常数。

## 5. 真实低投影还给逐头删除核近似

对低输出空间
$V_{m,Q}=\mathcal H_{\le Q}^{(m)}
\cap\ker(P_{\le Q-1}^{(m)}L)$，其每个 $v$ 满足
$$
 D^sv=P_{\le Q-s}^{(m)}(-A)^sv.
$$
第 $i$ 行在 $s=d-i$ 时准确为零。因此
$$
 \boxed{D^{d-i}v_i=0\quad(0\le i<d).}
 \tag{5.1}
$$
这保留整个向量的各尾孔层，不只保留顶部残量。

现取实际 $w\in M=\ker T$，令 $Q=q+d$，并把 $w$ 投到
$V_{m,Q}$。R239 低投影证明在这个稍宽窗口仍给
$$
 \|\widehat v-P_{\le Q}^{(m)}w\|
 \le e^{-74d^4}\|w\|.
 \tag{5.2}
$$
为核实没有越界：其辅助源上界为 $Q$、最大原像阶为 $d$，可用
(2.1) 的同一个放大 $R$；已证 $R\le2048q^2$，故
$\log(2+R)\le10+2\log q\le d^3$。
这是原低投影推导真正使用的条件，所以其进位 jet、$H_m(R)$ 和
$e^{-74d^4}$ 预算全部保持；没有直接把外观窗口 $Q$ 偷代进原宣告的
$Q\le e^{d^3/4}$。

在带 $q+1,\ldots,q+d$ 上令
$$
 P_{\rm ker}
 =\bigoplus_{t=1}^d\sum_{i=0}^{d-1}
 |e_i\rangle\langle e_i|\otimes P_{E_{d-i,q+t}}.
$$
由 (5.1)–(5.2)，
$$
 \boxed{
 \|(I-P_{\rm ker})P_{[q+1,q+d]}^{(m)}w\|
 \le e^{-74d^4}\|w\|.
 }
 \tag{5.3}
$$

## 6. 末端项转为准确的有限头长跃迁

现在 $v=P_{V_{m,q}}w$、$r=A v_q$，并用 (4.4) 的真实最优
$y,z_y$。把 $z_y$ 补成旧 $d$ 段输出链，取 $z_d=0$。记
$$
 g=D_0^*y-S_0^*z,\qquad
 f_y=P_{\mathscr C_{\rm flag}}g,\qquad
 \psi=y-\sum_{t=1}^{d-1}z_t .
$$
其中 $S_0$ 为旧全链内部输出，且
$\|S_0\|\le7$。因此
$$
 \|g\|\le\|y\|+7\|z\|\le8C^2\lambda.
 \tag{6.1}
$$
因为 $z_d=0$，完整 $L^*\psi$ 只有第 $q$ 层及这 $d$ 层，没有
第 $q+d+1$ 层的 $D^*z_d$。

对第 $t$ 层，令 $P_t=P_{W_{d-t+1}}$ 为允许的头投影。源
$D_0^*y$ 和前一段 $D^*z_{t-1}$ 已在允许头范围内；因此只有
$-A^*z_t$ 能越过此头界。定义原头算子
$$
 \boxed{
 H_t=P_{W_{d-t}}A(I-P_{W_{d-t+1}})
 \quad(1\le t\le d-1).
 }
 \tag{6.2}
$$
其所有非零矩阵条目从 $j\ge d-t+1$ 到 $i\le d-t-1$，所以均跨越至少两格；$H_1=0$。

用 $Lw=(L-T)w$，逐层配对、再把 $g$ 分成联合旗投影、头界外部分和删除核界外部分，得到
$$
 \boxed{
 \lambda^2
 =-\langle P_{[q+1,q+d]}^{(m)}w,c^{\min}\rangle
  +\sum_{t=1}^{d-1}\langle H_t w_{q+t},z_t\rangle
  +\mathfrak e_{m,q}(w).
 }
 \tag{6.3}
$$
全部小项有实际统一界
$$
 \boxed{
 |\mathfrak e_{m,q}(w)|
 \le e^{-70d^4}\|w\|\lambda.
 }
 \tag{6.4}
$$

逐项预算如下。纯删除核投影余项由 (5.3)、(6.1) 至多为
$8e^{-74d^4}C^2\|w\|\lambda$；
真实进位项由
$\|L-T\|\le26e^{-80d^4}$、
$\|\psi\|\le2C^2\lambda$，至多为
$52e^{-80d^4}C^2\|w\|\lambda$；
原顶部投影余项至多为
$6e^{-74d^4}C\|w\|\lambda$。
使用 $C\le e^{d^4}$、$d\ge32$ 后，其和小于 (6.4)。

这些项没有使用全源 $G^{-1}$ 或旧未预算的伴随极小链。剩下的
(6.3) 中间和是准确真实头矩阵的配对。

### 6.1 只有最优对偶链的低删除核部分进入主通量

在第 $t$ 段，$H_t$ 只读取 $j\ge d-t+1$ 的头坐标。
§5 的 $\widehat v$ 在这些坐标满足
$$
D^{d-j}\widehat v_{q+t,j}=0,\qquad d-j\le t-1.
$$
因 $H_t$ 只作用于头，
$$
H_t\widehat v_{q+t}\in
H_{\rm head}\otimes E_{t-1,q+t}.
$$
令 $\mathcal P_{t-1}$ 是这个删除核的原正交投影（头因子恒等）。
由 (5.2)、$\sup_t\|H_t\|\le6$ 和 (4.4)，
$$
\left|
\sum_t\langle H_tw_{q+t},z_t\rangle
-\sum_t\langle H_tw_{q+t},\mathcal P_{t-1}z_t\rangle
\right|
\le6e^{-74d^4}C^2\|w\|\lambda.
\tag{6.5}
$$
这是直和 Cauchy--Schwarz，未另付段数 $d$。
因此 (6.3) 可把每个 $z_t$ 换成
$\mathcal P_{t-1}z_t$；合并原逐项常数后，误差仍可用
$e^{-70d^4}\|w\|\lambda$ 控制。
下一节两条通量界也同时适用于这条投影后的通量。

不能仅从纯删除关系声称这些对偶投影为零。
例如在原非均权纯尾 $D=\sum_jb_jE_j$，
若 $Df=0$，直接交换子计算给
$$
D^2D^*f=-2\sum_jb_j^3E_jf.
$$
对不同 $j,k$ 取 $f=b_ke_j-b_je_k$，右边为
$-2b_jb_k(b_j^2-b_k^2)\Omega\ne0$。
所以创建算子并不把 $\ker D$ 自动送入 $\ker D^2$；
最优对偶链所需的低核消去须另外证明。

## 7. 真正缺陷需要正的头跃迁通量

进一步取 $w\in W=M\ominus N$。旧实际线性提升应用于
$k=v-c^{\min}$，给 $n\in N$ 且
$$
 \|n-k\|\le e^{-75d^4}\|k\|,\qquad
 \|k\|^2=\|v\|^2+\lambda^2.
$$
因 $\langle w,n\rangle=0$、$\langle w,v\rangle=\|v\|^2$，有
$$
 \left|\langle w,c^{\min}\rangle-\|v\|^2\right|
 \le e^{-75d^4}\|w\|
      \sqrt{\|v\|^2+\lambda^2}.
 \tag{7.1}
$$
将其代入 (6.3)，原 Hilbert 正能量得到
$$
 \boxed{
 \left|
 \sum_{t=1}^{d-1}\langle H_t w_{q+t},z_t\rangle
 -(\|v\|^2+\lambda^2)
 \right|
 \le2e^{-70d^4}\|w\|
       \sqrt{\|v\|^2+\lambda^2}.
 }
 \tag{7.2}
$$
对固定非零缺陷沿全整数 $m(q)$ 有 $v\to w$。所以充分大的 $q$
满足 $\|v\|\ge\|w\|/2$，进而
$$
 \boxed{
 \operatorname{Re}
 \sum_{t=1}^{d-1}\langle H_t w_{q+t},z_t\rangle
 \ge(1-e^{-69d^4})(\|v\|^2+\lambda^2).
 }
 \tag{7.3}
$$
这把真缺陷的未闭能量准确压到有限头长跃迁。若某一步 $r=0$，取
$y=z=0$；对非零缺陷的充分大窗口，(7.2) 本身便排除这种情况。

## 8. 不能把剩余跃迁当成小进位

虽然每个 $H_t$ 跨至少两格，实际慢头本来就含这些跳跃，它们并非全由
$\eta_{m-1}$ 控制。例如 $t=d-1$ 时，(6.2) 包含原条目
$$
 \langle e_0,A_Ne_2\rangle=\tfrac14,\qquad
 \langle e_0,A_Ye_2\rangle=\tfrac14-\eta_0 .
 \tag{8.1}
$$
前者来自 $b_1N_1$；后者还包含
$Y_0=N_0-N_0^2+\cdots$ 的准确 $-\eta_0N_1$ 项。因此不能因头很大
就直接吸收 (7.3)。

本稿已经支付特殊源正 Gram 的严格下界、极小对偶范数、真实进位和全部删除核投影误差。剩余问题是控制 (7.3) 中真正最优旗链与这些有限头跳跃的配对。仅用
$\|z\|\le e^{2d^4}\lambda$ 和普通 Hilbert 尾仍不足以使通量消失。
无权 $N=M$ 及普通 ISP 继续开放。
