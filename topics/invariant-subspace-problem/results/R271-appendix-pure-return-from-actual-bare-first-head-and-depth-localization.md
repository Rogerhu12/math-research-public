# R271 附录：实际裸首头的纯高返回 Schur 与深段局部化

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220。AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 对同一个原源的真正裸最小链，本文用其实际首物理头坐标给出纯高修复的准确投影和 Schur 公式；这次没有允许低域随完整最小化一起改变。原两高度泄漏给未来首头前 $K$ 段的纯费用
$2(K-2)S_m\Phi_{K-1,m}^2$。因此可以直接支付原实际纯返回的低深度部分，并把余量定位到真实裸首头的深段尾。

在原共同 good top 上，取 $H\asymp d^{3/4}$，低深度纯返回有明确指数小界。若原源还在前 $h\le H$ 个物理头，则剩余深段首头只来自真正 $\mathcal G^\dagger\zeta$ 的第零头、深 jet；真幂底项在这些段严格为零。没有断言该真实深段尾已小，也没有把源前缀传成整个 $\mathcal G^\dagger\zeta$ 的头支撑。普通 ISP、原 $N=M$ 和最终实际高返回比较仍 OPEN。

依赖：[同一首物理头的完整／裸共同商](R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md) §§1–2、5–6、[原准确两道桥](R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)、[逐列低高度泄漏](R271-appendix-columnwise-low-height-leakage-and-sharp-cubic-log-common-cost.md)、[R249 平衡相似](R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md)。

## 1. 原高域及同一个真正裸首头

固定原 $m\ge5,d=2^m,A=A_m,D=D_m$ 和全部合法 $q$。
记原完整未来右输入为 $\mathscr V_R$，其低／高出生正交分解为
$$
\mathscr V_R=\mathscr V_L\oplus\mathscr V_H.
$$
第 $t$ 段的高出生尾旗为 $E_{t-1,q+t}$；头和上端尾旗始终保原联合域。
令 $P_L,P_H$ 为这些原物理投影。
内部约束算子在低、高输入上的相关块仍记为
$\mathsf S_L,\mathsf B,\mathsf S_H$。

同一个原源 $r$ 的真正裸最小链记为 $a=a(r)$，有
$$
\mathsf S_La=0,\qquad \|a\|=\alpha(r).
$$
原两桥分解为
$$
a=b-\mathcal I\psi,\qquad
\psi=\mathcal G^\dagger\zeta(r),\qquad
\mathsf B a=-\mathcal R\psi.
\tag{1.1}
$$
所以当前真正需要估计的纯高向量是
$$
\boxed{
z_{\rm pure}(r)=
\mathsf S_H^\dagger\mathcal R\mathcal G^\dagger\zeta(r)
=-\mathsf S_H^\dagger\mathsf B a(r).
}
\tag{1.2}
$$
这是固定同一裸链后的高域最小修复，不是新 $H_2^\circ$ 的完整低高联合修复。

未来首头的原低空间、高出生空间及其完整和为
$$
\mathscr F_{\rm lo}
=\bigoplus_{s=1}^{d}
(E_{d,q+s}\cap E_{s-1,q+s}^{\perp}),
$$
$$
\mathscr F_{\rm hi}
=\bigoplus_{s=1}^{d}E_{s-1,q+s},\qquad
\mathscr F_{\rm full}=\mathscr F_{\rm lo}\oplus\mathscr F_{\rm hi}.
\tag{1.3}
$$
对 $s=1$，高出生项是零。
取真正裸首头
$$
\boxed{
f_r=-e_0^*a(r)\in\mathscr F_{\rm lo},\qquad
\|f_r\|\le\alpha(r).
}
\tag{1.4}
$$

令 $V=V_m$ 是原一致归一链基，$AV=VJ_d$、
$V=1\oplus V_+$。对未来首头数据 $f$，在未来外补零，定义
$$
\mathcal T_{\rm full}f
=P_{>q}\sum_{j=0}^{d-1}(Ve_j)(-D)^jf.
\tag{1.5}
$$
原共同商稿已完整证明该映射保持全部原右旗，
参数化所有零内部输出完整链，逆恰是第零物理头观察。
特别
$$
P_L\mathcal T_{\rm full}f
=\mathcal T_{\rm lo}P_{\mathscr F_{\rm lo}}f,\qquad
\mathcal T_{\rm lo}f_r=-a(r).
\tag{1.6}
$$
因此 $-\mathcal T_{\rm full}f_r$ 是同源真正完整候选，且其低部分准确为原 $a(r)$，没有重选裸最小者。

## 2. 纯高最小向量的准确投影与 Schur

定义
$$
\mathcal H=P_H\mathcal T_{\rm full}|_{\mathscr F_{\rm lo}},
\qquad
\mathcal T_H=\mathcal T_{\rm full}|_{\mathscr F_{\rm hi}}.
\tag{2.1}
$$
高出生首头空间在 $D$ 下不变，并被首源映射杀掉。
故 $\mathcal T_H$ 的像在 $\mathscr V_H$ 中，且
$$
\boxed{\operatorname{Ran}\mathcal T_H=\ker\mathsf S_H.}
\tag{2.2}
$$
正向由 (1.5) 的零内部输出和高域保持得到。
反向，任意 $h\in\ker\mathsf S_H$ 作为完整链也是零内部输出链；
其首头属于 $\mathscr F_{\rm hi}$，(1.5) 的唯一参数化给
$h=\mathcal T_H(e_0^*h)$。

又 $e_0^*\mathcal T_H=I$，所以
$$
\|\mathcal T_Hg\|\ge\|g\|,\qquad
\Gamma_H=\mathcal T_H^*\mathcal T_H\succeq I.
\tag{2.3}
$$
这保证其像闭，并给原正交投影
$$
P_{\ker\mathsf S_H}
=\mathcal T_H\Gamma_H^{-1}\mathcal T_H^*.
\tag{2.4}
$$
由 (1.6)，候选的高部分 $-\mathcal Hf_r$ 满足
$\mathsf S_H(-\mathcal Hf_r)=-\mathsf B a(r)$。
在同一个高域可行仿射空间中投掉 (2.2)，准确得到
$$
\boxed{
z_{\rm pure}(r)
=-(I-P_{\ker\mathsf S_H})\mathcal H f_r
=:\mathcal P f_r.
}
\tag{2.5}
$$
因而纯费用有完整原 Schur 式
$$
\boxed{
\|z_{\rm pure}(r)\|^2
=\left\langle
\left[
\mathcal H^*\mathcal H
-\mathcal H^*\mathcal T_H\Gamma_H^{-1}
 \mathcal T_H^*\mathcal H
\right]f_r,f_r\right\rangle.
}
\tag{2.6}
$$
这里消去的仅是纯高域零源自由量；裸首头 $f_r$ 固定。
所以 (2.6) 不会把允许低域变化的 $H_2^\circ$ 能量冒作纯能量。
其费用不大于 $\|\mathcal Hf_r\|^2$，只是可用上界。

## 3. 实际首头的低深度纯修复

令 $\Pi_{\le K}$ 按首头孔段 $1\le s\le K$ 截断，
$2\le K\le d$。由 (1.5)，
$$
(\mathcal H f)_t
=\sum_{j=1}^{d-t}
(-1)^j(Ve_j)P_{E_{t-1,q+t}}D^jf_{t+j},
\quad 2\le t\le d-1.
\tag{3.1}
$$
第 $t=1$ 段的高域为零；零次项因 $f_t\perp E_{t-1}$ 也为零。

原两高度泄漏引理应用于 $t-1$ 给
$$
\|P_{E_{t-1}}D^j(I-P_{E_{t+j-1}})\|
\le j\nu_m^{j-1}\sqrt{(t+2j-2)S_m},
\tag{3.2}
$$
其中 $\nu_m=\|D_m\|\le1/m$、
$S_m=\sum_{\ell\ge m}(\ell+1)^{-4}\le1/(3m^3)$。
本式准确适用于 $f_{t+j}\perp E_{t+j-1}$。

若 $t+j\le K$ 且 $t\ge2$，则 $j\le K-2$，
$t+2j-2\le2(K-2)$。
对每个 $j$ 在整链直和中，每个输入只出现一次。
于是定义
$$
\Phi_{K-1,m}
=\sum_{j=1}^{K-2}j\|Ve_j\|\nu_m^{j-1},\qquad
\vartheta_{K,m}^2
=2(K-2)S_m\Phi_{K-1,m}^2,
\tag{3.3}
$$
对 $K=2$ 两者均按零取值，就有
$$
\boxed{
\|\mathcal P\Pi_{\le K}f_r\|
\le\|\mathcal H\Pi_{\le K}f_r\|
\le\vartheta_{K,m}\|\Pi_{\le K}f_r\|
\le\vartheta_{K,m}\alpha(r).
}
\tag{3.4}
$$
特别 $\mathcal P\Pi_{\le2}=0$，而
$\vartheta_{3,m}^2=2S_m$。

对一般实际源，(2.5) 现在准确分解为
$$
\boxed{
z_{\rm pure}(r)
=\mathcal P\Pi_{\le K}f_r+
 \mathcal P\Pi_{>K}f_r,\qquad
\|z_{\rm pure}(r)-\mathcal P\Pi_{>K}f_r\|
\le\vartheta_{K,m}\alpha(r).
}
\tag{3.5}
$$
两个部分都是同一实际 $f_r$ 的线性截断，不是另选一个 bad primitive。
截断后的裸链不必是其各自源的最小者；证明没有用这个额外断言。

## 4. 三次对数实际首头深度上的纯小量

真实逐列界 $\|Ve_1\|=1$、$\|Ve_j\|\le e^{134j^4}$ 已在逐列泄漏稿 §4 证明。取
$$
J_m^{\rm fast}=\max\left\{1,
\left\lfloor(\log m/268)^{1/3}\right\rfloor\right\},
\qquad K_m^{\rm fast}=J_m^{\rm fast}+2.
$$
逐项预算与该稿 §5 相同，给
$$
\boxed{
\vartheta_{K_m^{\rm fast},m}^2
\le\frac{50J_m^{\rm fast}}{3m^3}
\quad(m\ge16).
}
\tag{4.1}
$$
若使用更宽
$$
J_m^{\rm wide}=\max\left\{1,
\left\lfloor(\log m/134)^{1/3}\right\rfloor\right\},
\qquad K_m^{\rm wide}=J_m^{\rm wide}+2,
$$
则在 $J_m^{\rm wide}\ge2$ 时
$$
\boxed{
\vartheta_{K_m^{\rm wide},m}^2
\le\frac{3\log m}{67m}\longrightarrow0.
}
\tag{4.2}
$$
回退 $J=1$ 时直接用 $2S_m$。

因此，如果真正 $f_r$ 恰支持在上述首头深度中，
这些就是整个原纯高费用的界；不需要低域重选。
对一般 $f_r$，它们只支付 (3.5) 的低深度项。
源在前 $K$ 个物理头并不自动给这里的首头深度支持。

## 5. dyadic 深度的一侧成本与实际 good-top 低块

设 $H=2^n$、$3\le n\le m$。
R249 给
$$
A_n=\Sigma_n(\gamma_nJ_H)\Sigma_n^{-1},\quad
\gamma_n=e^{20-\mathcal L_n},\quad
\mathcal L_n=\frac{25H^4}{2(H-2)},\quad
\|\Sigma_n\|\le H6^H.
$$
归一唯一性给同一个 $V$ 的前缀列
$Ve_j=\gamma_n^{-j}\Sigma_ne_j$。
所以不付逆条件数，直接有
$$
\begin{aligned}
\Phi_{H-1,m}
&\le H6^H\sum_{j=1}^{H-2}j\gamma_n^{-j}\nu_m^{j-1}\\
&\le H^3 6^H\gamma_n^{-(H-2)}
\le \exp\left(\frac{25}{2}H^4\right).
\end{aligned}
\tag{5.1}
$$
末个不等式使用
$(H-2)(\mathcal L_n-20)=25H^4/2-20H+40$
和 $3\log H+H\log6-20H+40<0$，后者对 $H\ge8$ 成立。
因而
$$
\boxed{
\vartheta_{H,m}
\le\sqrt{2(H-2)S_m}\,
 \exp\left(\frac{25}{2}H^4\right).
}
\tag{5.2}
$$
取 $H=d$ 还给所有源、所有合法 $q$ 的真实纯返回上界
$$
\boxed{
\|\mathsf S_H^\dagger\mathcal R\mathcal G^\dagger\zeta(r)\|
\le\sqrt{2(d-2)S_m}\,e^{25d^4/2}\alpha(r).
}
\tag{5.3}
$$
这里算子 $\mathsf S_H$ 中的下标表示原高域，与截断维数 $H$ 是不同记号。
(5.3) 只估计显示的实际裸链返回，不宣称任意高输出上的
$\|\mathsf S_H^\dagger\|$ 具有同一改进。
它仍是 $e^{O(d^4)}$ 费用，单靠此界不能完成窗口比较。

现在取原共同 good top，假设已付
$$
K_{\rm win}\ge \frac{e^{d^3/4}}{8d},\qquad
\alpha(r)\le\frac{2\varepsilon_m}{\sqrt{K_{\rm win}}}.
\tag{5.4}
$$
这涵盖与固定有限测试联合选切口时的预算。
对 $m\ge10$ 取
$$
H_m=2^{\lfloor3m/4-2\rfloor},\qquad
\frac18d^{3/4}<H_m\le\frac14d^{3/4}.
\tag{5.5}
$$
由 (3.5)、(5.2) 及 $S_m\le1/(3m^3)$，
$$
\boxed{
\|z_{\rm pure}(r)-\mathcal P\Pi_{>H_m}f_r\|
\le
8\sqrt{\frac{H_md}{3m^3}}\,
\exp\left(-\frac{39}{512}d^3\right)\varepsilon_m.
}
\tag{5.6}
$$
这里没有假定实际 $\varepsilon_m$ 有额外下降速率。
即使 $f_r$ 含所有原头和所有原段，显示的低深度纯高输出也已经支付。

## 6. 低物理源时，余深段只读取实际第一桥的第零头

若原源 $r\in\mathscr R_q\cap\ker A^h$，
真幂链满足 $b_s=0$ 对所有 $s>h$。
由 (1.1)、(1.4)，对于任何 $K\ge h$，
$$
\boxed{
\Pi_{>K}f_r=\Pi_{>K}e_0^*\mathcal I\psi,
\qquad \psi=\mathcal G^\dagger\zeta(r).
}
\tag{6.1}
$$
因此 (3.5) 严格变为
$$
\boxed{
\|z_{\rm pure}(r)-
 \mathcal P\Pi_{>K}e_0^*\mathcal I
 \mathcal G^\dagger\zeta(r)\|
\le\vartheta_{K,m}\alpha(r).
}
\tag{6.2}
$$
原 primitive 等距坐标逐段写为
$$
(\mathcal I\psi)_s
=(-1)^{s-1}J_{s-1}H_{s-1}^{-1/2}\psi_{s-1}.
$$
所以 (6.1) 的余量只读取实际 $\psi_{s-1}$ 的第零物理头和 $s>K$ 的深 jet。
该式不是把整个 $\psi$ 限制到一个源头旗；
低段中可能存在的跨头 $\psi$ 已由真实首头完整补全和纯高正交投影一并处理。

## 7. 一个完整保留的实际深段尾充分条件

为显示剩余费用，令 $H_0=2^{n_0}\ge8$，
$\Delta_nf_r=\Pi_{(2^{n-1},\,2^n]}f_r$，$n_0<n\le m$。
由 (3.4)、(5.2) 对每个实际首头段壳使用同一 $\mathcal P$，
再以 $\sum_{k\ge1}2^{-k}=1$ 作 Cauchy，得
$$
\boxed{
\|\mathcal P\Pi_{>H_0}f_r\|^2
\le
2S_m\sum_{n=n_0+1}^{m}
2^{n-n_0}(2^n-2)e^{25\,16^n}
\|\Delta_nf_r\|^2.
}
\tag{7.1}
$$
这是同一个实际裸最小者的加权深段条件。
若 $r$ 的物理头数不超过 $H_0$，可在右边用
$\Delta_ne_0^*\mathcal I\mathcal G^\dagger\zeta(r)$ 完全替换
$\Delta_nf_r$，由 (6.1) 该替换是准确身份。

本文没有证明 (7.1) 的右边对实际余源族趋零或可求和。
小的 $\|\psi\|$、小的完整 $H_2^\circ$ 能量，或者源的物理低头支撑，
都不能单独删除这里的权重。真正固定测试的伴随误差
$e_p$ 及其端点右费用也仍须另行支付。
