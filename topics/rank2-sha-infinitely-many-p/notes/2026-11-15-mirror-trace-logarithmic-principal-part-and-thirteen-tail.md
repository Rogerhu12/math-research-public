# 原镜轴迹的对数留数代表、真实主部延拓门与十三行尾带

日期：2026-11-15。**状态：下列接口已证明；指定迹在实际镜轴核上的行依赖仍未解决。**

本注接 [R822](../results/R822-original-cartier-residue-descent-and-actual-ramification-trace.md)、
[R550](../results/R550-actual-ramification-koszul-quotient-and-full-third-kernel-image.md)
及 [R808](../results/R808-original-third-precision-corrector-split-branches-and-near-normal-jet.md)。
只使用同一原来源 $qt^rF\mathcal H_2$ 和同一个修正 $R$。
将其有限分歧迹换成对数留数后，能够准确列出一个候选 Serre 主部的延拓条件；
该延拓条件本身不等于迹泛函已落入原 $\alpha_\eta^*$ 的像。

## 1. 同一来源及两种真实长度

保持
$$
p=6s-1,\quad s=2h+r,\quad 1\le r<h,\quad k_{\rm carry}=0,
\qquad e=\mathcal EF=YF_Y,\quad N=\mathcal O_C(C),
$$
其中 $C=(F=0)$ 是原十九角曲面上的整曲线，
$P=(0,1)$ 光滑且 $e(P)\ne0$，
$\mathcal H_j=H^0(X,\mathcal O_X(jC))$。
$F,e$ 及所有系数均使用原有理框，不重新选择一个可以删极的全局规范。

为免与镜轴的长度标号混淆，将原因子余项记为 $q_{\rm src}$。
准确变化列是
$$
\Delta R=q_{\rm src}t^r F H,\qquad H\in\mathcal H_2.
\tag{1}
$$
这个整块已经返回原 $\mathcal W_D$；保持原首修正还须满足其全部实际 jet 条件。

设
$$
W_s=t^{r+1-s}(1-t)^{3s},\qquad
A=W_s F_tq_{\rm src}t^r.
\tag{2}
$$
$F_t$ 指固定 $Y$ 的原偏导数。
把 R822 的固定非零标量 $3(-1)^s/17$ 暂从迹行中提出，定义
$$
\mathcal T(H)=
\sum_{Q\in Z^\circ}
\operatorname{Tr}_{\mathcal O_{Z_Q}/k}(A H),
\qquad Z_Q=(F,F_Y)_Q .
\tag{3}
$$
$Z^\circ$ 仅取原非固定仿射开集中的分歧概形；式中保非约化长度和全部残域迹。

真实相对 $J$ 长度及原 $M$ 的较短长度分别记为
$$
T_\Delta=s-r-\Delta,\qquad q_\Delta=T_\Delta-h,
\qquad \Delta=0\ \text{或}\ 13.
\tag{4}
$$
只在所用长度满足 R550 的 $h,q_\Delta>\kappa$、$T_\Delta\le2h$ 时调用其镜轴短正合列。
尤其原 primitive $M$ 第三精度通过 R808 才能进入 $\Delta=0$ 的同一个 $J$ 条件；
不能把任意第一次 $M\in p^2$ 改读为这个长窗口。

## 2. 该有限迹有一个完整对数留数代表

在 $C$ 的正规化上取原有理微分
$$
\Lambda_H=A\,H|_C\,\frac{de}{e}.
\tag{5}
$$
这里 $e$ 是原有理框中的函数，所以 $de/e$ 同时保它的零和极。
在 $Z^\circ$ 中一个光滑 $t$ 分歧点，分歧指数 $m<p$，
原方程给 $\operatorname{ord}(e)=m-1$。
于是
$$
\operatorname{Res}_Q\Lambda_H=(m-1)A(Q)H(Q),
\tag{6}
$$
经残域迹后正是 (3) 的局部代数迹。

若该开集中的 $Q$ 是原曲线奇点，则 $F_t(Q)=0$。
$A H$ 在每个正规化分支都正则且消失，
而 $de/e$ 在任意特征中至多有简单极，因此每个分支在 (5) 中的残数均为零。
同时 $A H$ 在局部 Artin 代数中的乘法算子幂零，迹也为零。
这个论证不宣称 R822 的一般 $\Xi_R$ 在各奇异分支分别无残数；
它只证明 (5) 对本篇因子倍子格给出了准确的总迹代表。

把 (5) 在 $P$ 之外、$Z^\circ$ 之外的全部分支残数和记为
$\mathfrak B_{\log}(H)$，始终作剩余域至 $k$ 的迹。
全局留数定理给
$$
\boxed{
\mathcal T(H)
=-\operatorname{Res}_P\Lambda_H-\mathfrak B_{\log}(H).
}
\tag{7}
$$
$\mathfrak B_{\log}$ 不是“仅十九个固定点”的缩写。
它包括原六个底纤维、十九个例外、两个水平框、
水平 $Y=0$ 上由 $F_0=\lambda d^cH_0(t)$ 的移动根产生的点、
原 $e$ 的全部真极、$q_{\rm src}$ 和各框的极，以及所有边界奇异分支。
原 $H_0(t)$ 此处是常数 charge 多项式，不能与变化列 $H$ 混淆。
若边界项重叠，就在同一正规化分支上合并读取一次。

在非边界、非分歧的仿射点，$e$、$A H$ 都正则且 $e$ 为单位，
故 (5) 正则。这样 (7) 已列尽所有可能项，没有省略 conductor 支或移动水平零点。

## 3. 同一镜轴条件与不能删去的短 M 尾

令 $\eta=\log(g/\psi)$ 为 R550 的真实轴偏移，$\operatorname{ord}_P\eta=h$。
记
$$
H^{(0)}=H|_C,\qquad H^{(1)}=(\mathcal EH)|_C.
$$
对实际
$$
H\in K_{\rm mir,T_\Delta}
=\ker\bigl[H\mapsto H(t,\psi e^{2\eta})\bmod t^{T_\Delta}\bigr],
$$
因 $T_\Delta\le2h$，准确存在同一个尾 $\epsilon_H\in k[[t]]$，使
$$
H^{(0)}+2\eta H^{(1)}=t^{T_\Delta}\epsilon_H.
\tag{8}
$$
$\epsilon_H$ 来自同一个 $H$；不能独立指定。

将 (8) 代入 (7)：
$$
\boxed{
\begin{aligned}
\mathcal T(H)
={}&2\operatorname{Res}_P
 \left(A\eta H^{(1)}\,\frac{de}{e}\right)
-\operatorname{Res}_P
 \left(A t^{T_\Delta}\epsilon_H\,\frac{de}{e}\right)\\
&-\mathfrak B_{\log}(H).
\end{aligned}}
\tag{9}
$$
在 $P$，$F_t,q_{\rm src},e$ 都按原框读取，$e$ 是单位；
$de/e$ 为正则微分，某个首导数因特征 $p$ 消失只会提高其阶。
由 (2) 得
$$
\operatorname{ord}_P A\ge 2r+1-s
=r+1-T_\Delta-\Delta.
\tag{10}
$$
因此 (5) 在镜轴核上的极阶至多
$$
q_\Delta+\Delta-r-1,
\tag{11}
$$
而 (9) 中第二项的微分系数阶至少
$$
r+1-\Delta.
\tag{12}
$$
当 $\Delta=0$ 时，第二项正则，故确实为零。
当只知道原短 $M$ 镜轴 $\Delta=13$ 时，其系数阶仅保证为 $r-12$：
$r\ge12$ 才自动无残数；
$1\le r\le11$ 时必须保留该尾的实际有限读取，最多读到正规单位乘积的 $t^{11-r}$ 项。
这正是完整十三行差，不能因写了镜轴或对数微分而删去。

## 4. 候选主部的唯一延拓判据

先只在已经支付的长窗口 $\Delta=0$ 中工作。
在 $P$ 的原 $N$ 局部框中，定义
$$
\omega_{\rm loc}=2A\eta\,de
\quad\text{作为}\quad
\omega_C\otimes N^{-1}
\quad\text{的局部亚纯截面}.
\tag{13}
$$
它的极阶至多 $h-r-1\le h$。
$\eta$ 只是实际形式轴，所以 (13) 只指定一个有限主部，
没有凭定义得到全局有理微分或全局截面。

令 $\mathscr L=\omega_C\otimes N^{-1}$。
由于 $\deg\mathscr L=-\chi<0$，有 $H^0(C,\mathscr L)=0$。
$C$ 为原整 Gorenstein 曲线，$P$ 光滑，因而主部短正合列和 Serre 对偶准确给：

**主部延拓判据。** (13) 的主部延拓为
$\omega\in H^0(C,\mathscr L(hP))$，当且仅当
$$
\boxed{
\operatorname{Res}_P\bigl(L|_C\ \omega_{\rm loc}\bigr)=0
\quad\text{对全部 }L\in\mathcal H_1.
}
\tag{14}
$$
若存在则唯一。

证明中用的是
$H^1(C,\mathscr L)^*=H^0(C,N)$，
以及原限制映射
$\mathcal H_1\to H^0(C,N)$ 满射、核恰为 $kF$。
后一事实来自
$0\to\mathcal O_X\to\mathcal O_X(C)\to N\to0$
和已付 $H^1(X,\mathcal O_X)=0$。
所以 (14) 使用整个原 $\mathcal H_1$，
不是任意环境多项式，也不是只测试常数一列。
奇点处用原对偶化层；不把正规化上允许的微分扩大为 $C$ 上的截面。

当只用 $\Delta=13$ 时，
(13) 的极阶可能超过允许的 $q_{13}=h-13$ 达 $12-r$。
同时 (9) 还有相同长度的尾项。
在 $r\le11$ 时不能把 (14) 直接换成较短 $q_{13}$ 的版本而忽略这两项。

## 5. 即使延拓成功，也没有单独杀掉迹

以下仍在 $\Delta=0$，故 $q_0=h$。
用 (8) 的正号选择 R550 的连接符号，
其真正 Serre 转置在 $B_0\in H^0(C,N^2(-hP))$ 上为
$$
\boxed{
\alpha_\eta^*\omega(B_0)
=
\operatorname{Res}_P
\left[
 \left(\frac{B_0}{2\eta}+(\mathcal EH)|_C\right)
 \frac{\omega}{e}
\right],
}
\tag{15}
$$
其中 $H\in\mathcal H_2$ 是同一个 $B_0$ 的真实全局提升。
改变提升 $H\mapsto H+FL$，(15) 改变量为
$\operatorname{Res}_P(L|_C\,\omega)=0$；
这一步使用的是 $\omega$ 已为全局允许截面，而不是任意局部主部。

若 (14) 成立，(13) 的实际延拓在 (15) 中给
$$
\alpha_\eta^*\omega(B_0)
=
\operatorname{Res}_P\left(A B_0\,\frac{de}{e}\right)
+
2\operatorname{Res}_P
\left(A\eta(\mathcal EH)|_C\,\frac{de}{e}\right).
\tag{16}
$$
两式只需主部相同，因为括号内与 $\omega$ 相乘的局部截面均正则。

在 $\ker\alpha_\eta$ 上，(16) 两项相消。
这不使第二项单独为零，更不使 (9) 的
$\mathcal T(H)$ 为零：第一项是同一个指定 $B_0$ 的值贡献，
$\mathfrak B_{\log}(H)$ 也仍保留。
因此不能将“候选主部可全局延拓”写成
$\mathcal T\in\operatorname{im}\alpha_\eta^*$。
要证明实际行依赖，尚须比较完整值项、整个边界泛函以及原低行右逆的高尾，
并在同一个 $H$／同一个 $R$ 的全部 normal 和 carry 上同时成立。

本注支付了 (5)、(9)、(14) 的精确接口，没有断言 (14) 当前全部为零。
没有新增中央零，没有扩大来源，没有把 $\mathcal H_3$ 的结论冒认整个 $\mathcal W_D$。
原 $P_{134}/U_0$、两个十三行 carry、同一 $P^{\rm fact}+pR$、
下一位 $p^2T$ 和指定 forcing 的真实非零问题均保持。


## 6. 增补：原 r=2 分类实际杀掉所有非固定 Y=0 移动项

这里继续使用当前原 $r=2$ 全分类，不另假设最高 charge 为 $S$-单位。
记 $q_0(t)=q_{\rm src}(t,0)$；
R792/R797 采用同一原固定角清分母后的因子规范：

* 若 $q_0\not\equiv0$，原因子的常数 charge 为 $F(t,0)=\lambda d^c$，
  所以非固定水平 $Y=0$ 上没有移动交点。
* 若 $q_0\equiv0$，准确有 $q_{\rm src}=Y^j q^\circ$，$j\ge1$。
  原 $F(t,0)=\lambda d^c H_0(t)$ 可有移动根，包括非单位 $H_0(0)$ 的情形；
  后者落在固定 $t=0$ 边界，仍按原边界读取。

现在取第二种情形中位于所有固定底纤维之外的
$Q\in C\cap(Y=0)$，并取其任意正规化分支 $\widetilde Q$。
在这个原仿射框中，$F_t,q^\circ$ 和每个
$H\in\mathcal H_2$ 都真正正则；
这是原全 Gauss 来源在非固定有限角没有分母的性质。
$W_s$、$t^r$ 为单位。因此
$$
\operatorname{ord}_{\widetilde Q}(A H)
\ge j\,\operatorname{ord}_{\widetilde Q}Y>0.
\tag{17}
$$
另一方面，任取正规化参数 $v$，写 $e=v^n u(v)$、$u(0)\ne0$，则
$$
\frac{de}{e}=n\,\frac{dv}{v}+\frac{du}{u}.
\tag{18}
$$
无论 $Q$ 是否奇异，也无论 $p$ 是否整除 $n$，
这个对数微分至多简单极；若 $p\mid n$，极项反而消失。
(17) 与 (18) 直接给
$$
\boxed{
\operatorname{Res}_{\widetilde Q}
\left(A H\,\frac{de}{e}\right)=0
\quad\text{对全部原 }H\in\mathcal H_2.
}
\tag{19}
$$
因此它也在实际 $K_{\rm mir,T_\Delta}$ 上为零；
不是通过扩大核或选择不同 $H$ 得到的。
各正规化分支分别为零，故全部剩余域迹均为零。

结合两种 $q_0$ 情形，当前原 $r=2$ 全分类下，
(7)、(9) 的 $\mathfrak B_{\log}$ 可以**准确删除非固定水平 $Y=0$ 的全部移动项**。
这是原 $q_{\rm src}$ 的正 $Y$ 因子所支付的消去；
不能把 (19) 扩到一般 $\Xi_R$、非因子倍来源，
也不能删掉 $t=0$ 等固定点、水平 $Y=\infty$ 的移动最高系数根、
真 $e$ 的其余极或两条十三行 carry。
剩余的联合边界仍须与同一个 $\alpha_\eta$、同一个 $R$ 一起比较。
