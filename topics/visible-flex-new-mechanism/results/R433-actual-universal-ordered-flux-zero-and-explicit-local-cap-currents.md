# R433：全部有序自然缺陷的实际联合零值与三阶局部 cap current

日期：2026-11-16。**完整纸面证明及已发表原值的消费；没有执行新的 profile、积分、符号程序、秩、科学运行或人工测试。**

[R431](R431-common-exterior-degeneracies-in-the-complete-four-constraint-nineteen-target-library.md) 已在同一个四约束、共同 $D,E_5$、十九根母库中保持全部内部 $A_f$ 退化点的共同外区。但实际有限自然查询为零，不能直接代替 [R405](R405-common-exterior-packets-and-local-ordered-currents-at-all-internal-degeneracies.md) 原 Euler-current 证明中的全输入恒等。

本文支付一个严格较弱、而又足够删除这项余差的 actual 条件：**全部有序 $3+2$ 自然系数为零**。它不要求全部 self 自然函数为零，也不与 R406 的正字符障碍冲突。

令 $\mathcal A$ 为 R429 的同一共同有限查询，另记
$$
\mathcal O(V)(u,v)=[s^3t^2]\Lambda_{su+tv}(V),
\qquad
\sup\operatorname{supp}u<\inf\operatorname{supp}v .
\tag{1}
$$
本稿证明，同一共同合法窗口前提下，
$$
J^+=(E,\mathcal A,\mathcal O),\qquad E=(\pi,\mathcal Q)
$$
有完整实际成本满锥和一个固定有限真实词的 $C^1$ 截面。因此可以在同一新实际几何上取
$$
\boxed{E=0,\qquad\mathcal A=0,\qquad\mathcal O=0.}
\tag{2}
$$
没有把分别取得的截面拼接，也不增加辅助包的 self 目标。

在(2)下，全部跨包 partial 有一个原右锚的显式局部 current，最高只到三阶 jet；在 $A_f=0$ 点，它只使用 $u,p=u',r=u''$。四个含 $u$ 的项和其余三个项在下文逐式列出。它们不是 R432 的 $c_\tau=0$ 响应列已经能任意改变的坐标；剩余真实响应像、self cap、全部内部条件及十三行同规范仍明确保留。

直接使用 R344、R352、R389、R405、R407、R413、R428、R429，以及 R428 已逐条消费的 R130/R140/R145/R188/R190/R206/R212/R323/R333/R350/R356/R382/R386/R406/R416/R419—R427。本文不重算这些原完整值。

## 1. 新增映射杀整个响应空间，不只杀其 whole-E 核

采用原自然规范
$$
\Lambda_u(V)=\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)).
\tag{3}
$$
$\mathscr G$ 是原 pure 有序 $2+2$ 的完整三矩尾映射，含全部右锚及原历史。

这里需要的精确来源是
[R344 §6—7](R344-general-pure-factorization-of-total-response-flux-with-ordered-Green-tails.md)：
其(34)对整个 $\mathcal R$ 给 self 收缩的 pure 加有序 Green 因子化，(37)—(38)给修正后的 annihilator。
[R352 §6—7](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)
再以完整原函数证明辅助三包独立性，其(23)—(24)正是
$$
\boxed{\Lambda_u(R)=0\quad
\text{对全部紧 }u,\ R\in\mathcal R.}
\tag{4}
$$
(4)没有要求 $\pi R=0$ 或 $\mathcal QR=0$。

$\Lambda$ 对输入为齐次五次多项式，故对 $su+tv$ 取普通系数直接得到
$$
\boxed{\mathcal O(\mathcal R)=0.}
\tag{5}
$$
因此原每一个同权 $E$ 响应补偿都没有新增 $\mathcal O$ 代价。
不能把未经修正的 $\Omega_u=\int u'''V(u^2,0)$ 用来替代(3)：它只在 $\pi V=0$ 后等于 $\Lambda_u$，否则真实 Green 项会改变这一步。

### 1.1 有限真实查询与准确仿射核

(1)取遍全部有序实紧输入，定义一个函数值线性映射；
其像仍有限维，因为原 $U$ 有限维。
可以顺次选择有限个真实有序对 $(u_\nu,v_\nu)$，使相应普通 $3+2$ 系数在这个像上忠实。只加入这些系数，不将用于系数提取的额外 self 评价独立列作目标。

这些测试对可取在同一个物理窗口内。原自然读出的仿射协变及有限真权/平移性质，使每个非零测试在共同正仿射参数中是有限 Laurent—多项式函数；它不能在一个非空安置开域上恒零。因此先压入有序的不交小窗再选有限忠实测试，不损失函数像。测试输入只用于原 universal 函数观测，不声称它们是首阶研究圆或新的合法轨道。

原自然协变给
$$
\mathcal O(\mathsf P_{H,c}V)(u,v)
=H^2\mathcal O(V)(C_{H,c}u,C_{H,c}v),
\quad H>0.
\tag{6}
$$
正仿射变换保留有序支撑，故 $\ker\mathcal O$ 是真仿射不变核。
原 $N$ 降真权，而 $U$ 的真权只在 $[-9,3]$，故平移作用是有限多项式；缩放作用是有限 Laurent 式。其平移生成元和全部有限真权投影也保持该核。
R145 的同右锚代数反号按各真权作用，因而也保持此核；
这里没有把物理反射换成另一积分锚。

## 2. 一般 whole-E 成本的非 Euler 部分可以完整显写

本节先只施加 $E(V)=0$，暂不假 $\mathcal O(V)=0$。

沿 R405 原完整恢复，任意外部三矩参数 $n$ 给
$$
Q_{V,n}(u)=L_{V,n}(x,u,p,r)
+\sum_{j=0}^2m_j(x,n)J_j(u),
\quad
\mathcal U_{V,n}=4Q_{V,n},
\tag{7}
$$
其中
$$
J_j'(u)=-j_j(u),\qquad
j_j=x^jr^2+2\mathbf1_{j=2}p^2.
$$
whole $\mathcal Q=0$ 给的是 $m_j''=0$，不把其仿射系数删掉。写
$$
m_j=\alpha_j x+\beta_j,\qquad
M=m_0+xm_1+x^2m_2,\qquad
A=\alpha_0+\alpha_1x+\alpha_2x^2,
$$
$$
L=\ell_0u^2+\ell_1up+\ell_2ur+
\ell_3p^2+\ell_4pr+\ell_5r^2 .
\tag{8}
$$
$\ell_j$ 关于 $x$ 的次数至多六；全部 $\ell_j,\alpha_j,\beta_j$ 是原成本和原 $n$ 的确定线性读出，保完整 $s$ history。下文撇号作用于显示的 $x$ 系数，$n$ 不被微分。

令
$$
\mathcal D_{V,n}(u)=p\,\mathcal U_{V,n}(u)''.
$$
定义以下局部三次密度：
$$
\begin{aligned}
\mathcal C_{V,n}(u)={}&
-\frac{\ell_0'''}3u^3
+\left(3\ell_0'+\frac{\ell_1''}2\right)up^2\\
&+\left(\ell_0+\frac56\ell_1'
+\frac13\ell_3''-\frac83\alpha_2\right)p^3\\
&-\left(\ell_1+\frac{\ell_2'}2\right)ur^2\\
&-\left(\frac{\ell_2}2+2\ell_3+
\frac{\ell_4'}2+A\right)pr^2\\
&+\left(M-\frac{\ell_4}2-\frac{\ell_5'}3\right)r^3.
\end{aligned}
\tag{9}
$$
这是完整 $C^2$ 密度，不是 principal。

为保留真正的 partial，而不只比较总积分，置
$$
\begin{aligned}
B_L={}&
\ell_0u^2r-\ell_0'u^2p-\ell_0up^2+\frac{\ell_0''}3u^3\\
&+\ell_1upr-\frac{\ell_1'}2up^2-\frac{\ell_1}3p^3
+\frac{\ell_2}2ur^2\\
&+\ell_3p^2r-\frac{\ell_3'}3p^3
+\frac{\ell_4}2pr^2+\frac{\ell_5}3r^3,
\end{aligned}
$$
$$
\boxed{
\mathcal K_{V,n}
=4\left[pD_xL-rL
-p(Mr^2+2m_2p^2)+B_L+\frac23m_2p^3\right].
}
\tag{10}
$$
直接真实分部积分给
$$
\boxed{
\mathcal D_{V,n}=D_x\mathcal K_{V,n}+4\mathcal C_{V,n}.
}
\tag{11}
$$

有尾项的关键一步可以单独核对：
$$
u'''m_jJ_j
=D_x(rm_jJ_j-pm_j'J_j)+(m_jr-m_j'p)j_j.
$$
把它与 $D_x(pQ'-rQ)$ 合并，所有 $J_j$ 恰消；
余 $2m_2p^2r$ 再给
$$
2m_2p^2r=D_x(2m_2p^3/3)-2\alpha_2p^3/3.
$$
连同原 $-2\alpha_2p^3$，正是(9)的 $-8\alpha_2p^3/3$。
局部的六项 $u'''L$ 则逐项给 $B_L$ 及(9)其余系数。
没有把 $J_j$ 的左值改成零；(10)在零 collar 为零，是 profile jets 的真实结果。

因此一般 whole-E 成本的完整 cap 值为
$$
\boxed{
\int_{\ell_u}^{x}u'\mathcal U_{V,n}''
=\mathcal K_{V,n}(x;u)
+4\int_{\ell_u}^{x}\mathcal C_{V,n}(u).
}
\tag{12}
$$
旧有限 $\mathcal A=0$ 确实给所有已选母及其共同仿射像上的整个积分零；
它不是(9)六个系数的字面零定理。
本文不从 $q,D,E_5$ 的已付五次 profile 条件推出这个三次 universal 身份。
下面通过一个同样可实际支付的新联合映射删除(12)的余积分。

## 3. 全有序零值准确等价于六条系数身份

现在施加 $E(V)=0$ 与 $\mathcal O(V)=0$。
R389 的 natural-to-raw 步骤先使用 $\pi V=0$，故对任意真实有序 $u<v$，
$$
\mathcal O(V)(u,v)
=\int u'''\mathcal U_{V,\mu(v)}(u)
=\int\mathcal D_{V,\mu(v)}(u).
\tag{13}
$$
两个 $x$ 分部只用紧 outer 的真零 jets。
对固定任意 $u$，其右方可以取三个同形同宽、中心不同的实包，
三个原矩向量组成可逆 Vandermonde 矩阵。
因此(13)为零准确给
$$
\int\mathcal D_{V,n}(u)=0
\quad\text{对全部紧 }u,\quad n\in\mathbb R^3.
\tag{14}
$$
任意 $n$ 在这里来自三条真实矩基的线性延拓，不声称它是一个正平方包的矩。

由(11)，$\int\mathcal C_{V,n}=0$ 对全部紧输入成立。
(9)的六个规范密度没有全导数线性关系：若
$$
c_0u^3+c_1up^2+c_2p^3+c_3ur^2+c_4pr^2+c_5r^3
$$
的 Euler 多项式为零，其最高 $u^{(4)}$ 系数是
$2c_3u+2c_4p+6c_5r$，先迫 $c_3=c_4=c_5=0$；
余 Euler 的 $r$ 系数再迫 $c_1=c_2=0$，最后 $c_0=0$。
这里各 $c_j$ 可以是任意光滑 $x$ 系数；使用真实自由紧 jets，不执行秩计算。

所以(14)准确等价于
$$
\boxed{
\begin{gathered}
\ell_0'''=0,\qquad \ell_1''=-6\ell_0',
\qquad \ell_2'=-2\ell_1,\\
\ell_3''=8\alpha_2-3\ell_0-\tfrac52\ell_1',\\
\ell_4'=-\ell_2-4\ell_3-2A,\qquad
\ell_5'=3M-\tfrac32\ell_4 .
\end{gathered}}
\tag{15}
$$
反过来，(15)令(9)字面为零，(11)、(13)也给 $\mathcal O=0$。
故这是原 whole-E 范围中的准确 iff，而非仅充分的生成表。

在(15)下，
$$
\boxed{
\int_{\ell_u}^{x}u'\mathcal U_{V,n}''
=\mathcal K_{V,n}(x;u).
}
\tag{16}
$$
(10)最高只到 $u'''$，显式 $x$ 次数至多六。
它与 R405 的齐次 Euler current 相差一个恒零锚定常数；
无需使用该稿保守的七阶 jet 表示。

### 3.1 在退化点的实际七项值

若 $A_u=6pt-2r^2=0$，其中 $t=u'''$，则 $pt=r^2/3$。
代入(10)并用(15)，得
$$
\boxed{
\begin{aligned}
\frac14\mathcal K_{V,n}\big|_{A_u=0}
={}&\frac{\ell_0''}3u^3
+\left(\ell_0+\frac{\ell_1'}2\right)up^2
-\ell_1upr-\frac{\ell_2}6ur^2\\
&+\frac23(\ell_3'+\ell_1-2m_2)p^3
-2(\ell_3+A)p^2r
+\left(2M-\frac23\ell_4\right)pr^2 .
\end{aligned}}
\tag{17}
$$
$r^3$ 项准确相消；没有除以可能为零的 $p$。
在实际简单 $A$ 点，原 $p$ 简单性本来也保证 $p\ne0$。

(15)使 $\ell_0,\ldots,\ell_5$ 的次数分别至多
$2,3,4,4,5,6$。
因此(17)七个系数的次数依次至多
$$
0,\ 2,\ 3,\ 4,\ 3,\ 4,\ 5.
\tag{18}
$$
固定真实宽度及外部 $n$ 后，根处 current 的中心次数至多五；
若整个实际布局同时平移，suffix 三矩另按原二次三角式输运，
完整次数可到七，不能把 $n$ 冻住误报。

前四个含 $u$ 的单项在(17)中明确保留。
R432 的 $c_\tau=0$ 列给的是 $p^3$ 乘其七个 $s=r/p,\ xs-1$ 函数；
(15)没有自行证明前四项为零，或证明它们落在那三十二条成本列的像内。
(17)是接下一真实响应比较的目标式，不是新的自由参数假设。

### 3.2 与原 c 零响应比较的十三个共同形式生成方向

由(15)，前三个系数准确写成
$$
\begin{aligned}
\ell_0&=A_0+A_1x+A_2x^2,\\
\ell_1&=B_0+B_1x-3A_1x^2-2A_2x^3,\\
\ell_2&=C_0-2B_0x-B_1x^2+2A_1x^3+A_2x^4 .
\end{aligned}
\tag{18a}
$$
这六个参数仍是原 $V,n$ 的确定线性读出，不称它们能由实际成本独立指定。

为给每个参数一个明确的形式代表，可在(15)中取
$m=0$，并把 $\ell_3$ 的常数/一次积分常数及 $\ell_4$ 的常数置零，得到
$$
\ell_3=-\left(\frac32A_0+\frac54B_1\right)x^2
+2A_1x^3+A_2x^4,
$$
$$
\ell_4=-C_0x+B_0x^2+2(A_0+B_1)x^3
-\frac52A_1x^4-A_2x^5 .
\tag{18b}
$$
把(18a)—(18b)逐个单位参数代入(17)，便定义六个完整形式列；
没有只取其含 u 部分而丢掉同列的 $p$ 部分。
它们尚未被宣称为原 $U$ 或 $\mathcal R_E$ 的成本代表。

减去这六列后，剩余 $\ell_0=\ell_1=\ell_2=0$。
此时(15)给
$\ell_3=d_0+d_1x+4\alpha_2x^2$，
再代(17)，其根值的共同形式空间恰由
$$
\boxed{
p^3,\quad p^2r,\quad xp^2r,\quad
pr^2,\quad xpr^2,\quad x^2pr^2,\quad
2xp^3-5x^2p^2r+3x^3pr^2
}
\tag{18c}
$$
生成。具体地，若 $\ell_4$ 的积分常数为 $e_0$，剩余 $\mathcal K/4$ 是
$$
\begin{aligned}
&(\tfrac23d_1-\tfrac43\beta_2)p^3
-2(d_0+\alpha_0)p^2r-2(d_1+\alpha_1)xp^2r\\
&+(2\beta_0-\tfrac23e_0)pr^2
+(\tfrac83d_0+\tfrac{10}3\alpha_0+2\beta_1)xpr^2\\
&+(\tfrac43d_1+\tfrac83\alpha_1+2\beta_2)x^2pr^2
+2\alpha_2(2xp^3-5x^2p^2r+3x^3pr^2).
\end{aligned}
$$
这些形式参数给全部七个方向；其中
$(d_1,\alpha_1,\beta_2)$ 到 $p^3,xp^2r,x^2pr^2$ 三系数的行列式为 $8/9\ne0$，
其余四方向可直接逐项指定。
最后一项的三系数由同一个 $\alpha_2$ 决定，不能拆成三个自由方向。
令 $s=r/p,\ t=xs-1$，(18c)正是 $p^3$ 乘 R432 的
$1,s,t,s^2,st,t^2,xt(3t+1)$ 的同一空间。

六个形式列的含 u 部分模(18c)线性独立：
$u^3$ 系数先给 $A_2=0$；
$up^2$、$upr$ 的自由 jets 再给 $A_1,A_0,B_0,B_1=0$；
最后 $ur^2$ 给 $C_0=0$。
因此通用形式空间是十三个生成方向；
它不是某个实际根配置上十三行满秩的声明。

相对于 R432 已列的 c 零跨包 current，尚需研究的含 u 部分最多是
这六参数对 $n_0,n_1,n_2$ 的十八个系数。
同一个成本的这些系数还受原 $U$、whole E 与几何历史关系约束。
本文不把十八个生成位置当成真实秩，也不从形式代表宣布它们全可控。

## 4. 为什么新增全部 O 后仍没有正仿射字符

固定 R429 的同一实际母库及共同 $\mathcal A$，置
$$
\mathcal A^+=(\mathcal A,\mathcal O),\qquad
J^+=(E,\mathcal A^+).
\tag{19}
$$
不改变原十九根、四母约束及共同 $D_0,E_0$。
新增的 O 测试不要求其辅助输入自身具有这些值，因为只加入有序系数。

由(5)，所有同权 $E$ 响应补偿对 $\mathcal A^+$ 均为零。
具体在下述负六、负四字符步骤中，取 $\sigma\in\{-6,-4\}$。若 $V\in U_\sigma,Z\in U_{\sigma+1}$ 满足
$\mathcal A^+(V)=\mathcal A^+(NZ)$ 时，
R323 给真实 $R_V\in\mathcal R_\sigma$ 使
$E(R_V)=E(V-NZ)$。于是
$$
J^+(V-NZ-R_V)=0.
\tag{20}
$$
任何经此同一个 $J^+$ 下降、杀响应与平移的字符都满足
$\lambda(V)=0$。
这里仅消费 R323 在这两个权上已付的 $E$ 响应等像，不声称全权 $E(U)=E(\mathcal R)$。不能只用旧 $\mathcal A$ 相等去删一个新的纯 O 字符；
以下逐条说明所有所用身份已经在 $\mathcal A^+$ 中成立。

若一个完整自然函数是局部五次密度，则对不交 $u,v$，
$\Lambda_{su+tv}=s^5\Lambda_u+t^5\Lambda_v$，故其 O 为零。
本稿只对已经证明完整 locality 的下列原函数使用这一点，不声称整个 $U$ 自然局部：

| 原完整族或层 | 已付自然函数范围 | 新增 O |
|---|---|---|
| 全 Abar、修正后全 H | R350/R382 的 universal 零 | 零 |
| 全 Q4 | R386 的完整局部五次密度 | 零 |
| 整个真权0 | R406 的 $\lambda_+ n_2$，$n_2$ 完整局部 | 零 |
| 整个真权 $-8$ | R356 的 universal 自然零 | 零 |
| 权 $-6$ 的全曲率 static、hh | R416/R419 的 universal 自然零 | 零 |
| 权 $-6$ 全曲率 kk | R421 的完整局部 $(1+k^2)^2(5pr^4-3xr^5)/640$ | 零 |
| 权 $-4$ 全曲率 static | R417/R420，余 $W_4$ 零，完整像为局部 Q4 行 | 零 |
| 权 $-4$ 全曲率 hh | R425 的 $-3(1+k^2)^2F_{Q4}/16$ | 零 |
| 权 $-4$ kk 的 $V_0,V_2,V_4$ | R426/R429：前两完整局部，末者零 | 零 |

这些都是原势、$\Gamma$、两种 true tail 和正规化之后的完整结论；
没有将 raw self 的主部充作本表。

特别原 Q4 的全部共同 $D/E_5$ 平移链在新增 O 上恒为零。
令原 $W_H\in U_{-3}$ 表示该链的 H 槽，R429 的身份遂提升为
$$
\mathcal A^+(V_2)
=-\frac{D_0+3E_0}{96(E_0-D_0)}
\mathcal A^+(NW_H),\qquad
\mathcal A^+(V_4)=0.
\tag{21}
$$
右侧和左侧的 O 都准确零，不是因旧 self 值比例而猜测。
$V_0$、全 static 与 hh 所用的 Q4 比较也完全同样提升。
$D_0-E_0>0$ 保原分母非零；没有新增 $M_{25}$ 条件。

### 4.1 六种可能字符都在这个同一联合像中排除

$J^+$ 的核仿射稳定。R127/R145 的真实锥与单权提取仍将非零正字符限于
$$
-8,-6,-4,-2,0,2 .
$$

- $-8$：整自然零，故 $\mathcal A^+=0$；同权 $E$ 响应等像经(20)排除。
- $0$：原各母全部 affine $n_2$ 为零，完整 locality 杀所有实际 ordered 行，也杀新增 O。因此 $\mathcal A^+(U_0)=0$，R333 给 $J^+(U_0)=J^+(\mathcal R_0)$。
- $2$：R190 的原完整 $U_2=\mathcal R_2$ 直接排除。
- $-2$：R188 已排除整个真实 $U$ 上该权的正仿射字符；不依赖本稿新商。
- $-6,-4$：表中 Abar/H 与全 Q4 的共同链，经(20)先使最高几何导数层的字符值为零。R140/R413 才给同一个原乘子，使完整剩余 action 为逐态 static 非负及 Q2 正半定。

负六中，R416 的全 static 和乘子零式在新商仍成立；
R419 的 hh 值为零，PSD 迫字符的 hk 值为零；
R421 的 kk 局部式在偶母 $M_5=0$ 的全部实际 affine self 为零，
其全部 ordered 行和新增 O 也零。
故整个 kk 的字符值为零。

负四中，R420 的全 static action 与乘子零式同样保持；
R425 的 hh 落原 Q4 平移像，故字符值为零，
PSD 再迫 hk 字符值为零。
原 $V_0$ 与(21)清全 kk。

这里没有先声明 $\mathcal O(hk)$ 本身为零；
需要的是同一个正半定矩阵在对角字符值零后其交叉字符值零。
原 R130 十四个完整正规族及响应已穷尽，这些逐层零值迫字符为零；
因此没有遗漏一个只看新增 O 的正字符。

令 $\mathcal S$ 为原实际同 scalar/frame 端口、$M=\mathbf T=0$ 的块，
得到
$$
\boxed{
\overline{\operatorname{cone}J^+(\mathcal S)}=J^+(U).
}
\tag{22}
$$

## 5. 同一个有限实际 C1 截面，全部基准重新入账

定理的实施前提与 R428/R429 相同：
原母库、有限 O 测试、右锚、全部有限原型、桥与紧参数包络，
须从起点置于同一个共同合法物理窗口。
必要时先作一次共同正仿射识别，目标按同一可逆映射输运，
零目标保持零；求根后不移动 profiles，不放宽旧冻结窄窗口。

在此前提下，对 $J^+(U)$ 的任意紧相容目标集，
存在一个固定有限真实词族 $\mathscr D(y)$，满足
$$
\boxed{
M_{\mathscr D}=\mathbf T_{\mathscr D}=0,\qquad
J^+(V_{\mathscr D(y)})=y,
}
\tag{23}
$$
并对 y 为 $C^1$。目标空间是实际联合像，不是未经证明的直积。

证明重作 R206/R212 的同一个真实词，不能把 R429 的截面与另一 O 截面相加。
记
$$
\mathscr P^+=J^+(U),\quad
\mathscr L^+=J^+(\mathcal R),\quad
q:\mathscr P^+\to\mathscr P^+/\mathscr L^+ .
$$
由第4节的整个零权等像，缩放生成元在此响应商上可逆。
(22)选出有限实际块及严格正核
$\sum\alpha_i qJ^+(V_{B_i})=0$，$\alpha_i>0$。

用真 $M=0$ 桥和同一桥的真实倒行拼
$$
A_i(t_i)(B_i^{e^{t_i}})^{n_i}A_i(t_i)^R.
$$
其完整成本为
$$
2V_{A_i(t_i)}+n_i\mathsf P_{e^{t_i},0}V_{B_i}.
\tag{24}
$$
桥的 O、E 和有限 A 基准全部留在这同一个式子中。
取 $n_i=\lfloor N\alpha_i\rfloor$ 后，原商方程的真实 $C^1$ 极限、可逆缩放 minor 及一个固定有限 N 给紧目标商截面。

再取响应基及其真实第三原型。先用上述**整个新商**截面清每个原型成本的商基准；其剩余响应成本不删。
共享原型和真倒行词给
$$
J^+(V_{Z(t,n)})
=E_0(t)+n\left(2\sum_\ell J^+(\widehat v_\ell)
+\sum_\ell t_\ell J^+(K_\ell)\right).
\tag{25}
$$
这里 $qJ^+(\widehat v_\ell)=0$，故 $qE_0(t)$ 与最后 n 无关。

对每个目标 y，再接一个实际新商校正块，
准确清 $qy-qE_0(t)$。固定所有第二批整数后，响应坐标仍是
$$
n(a+t)+F(t,y),
$$
其中 F 保留 $E_0(t)$ 和第二次校正块的**全部**响应基准。
在先固定的紧盒上 $F,D_tF$ 有界且与最后 n 无关。
选一个有限 n 使
$$
t=-a+n^{-1}(\ell y-F(t,y))
\tag{26}
$$
为统一收缩，得到(23)的同一个 $C^1$ 根。

有限忠实 O 测试是固定光滑 profile 的原函数查询；
普通多项式系数提取也是固定线性操作。
原 R56 在有限真实词上的积分及恢复给其 $C^1$ 性。
因此此处不以抽象有限维代替实际几何正则性。

固定 hook/保护芽与 Klein 背景若从起点纳入同一真实包络，
最终成本是 $V_{\rm base}+4V_{\mathscr D}$。
准确取目标 $-J^+(V_{\rm base})/4$，同时支付(2)。
两个 quotient 校正及最后响应重复都在同一库上完成；
不继承旧几何的 incoming history、Morse 或未付 metric 条件。

## 6. 与 universal 自然正障碍相容

R406 的原 signed 类满足
$$
E(H_*)=0,\qquad
\lambda_+(H_*)=1,\qquad
\Lambda_u(H_*)=n_2(u).
$$
R431 各母的整个 affine $n_2$ 为零，
其完整 locality 又使所有实际 ordered 行与(1)全为零。
所以
$$
\boxed{J^+(H_*)=0,\qquad\lambda_+(H_*)=1.}
\tag{27}
$$
这个核见证不是实际路径，但它准确说明原正字符不能经本联合映射下降。
新实际(2)仍允许在别的输入上有非零 self 自然值；
没有构造被 R406 禁止的 universal $\Lambda_{\rm all}=0$ 成本。

事实上新加的是全 ordered，而原 self 部分仍只保留 R429 的有限共同 A。
不要把这些量合称“全自然已零”。

## 7. 同一个实际圆的所有跨包 cap 现在真为局部 current

消费(2)后，R431 的全部 roots、宽度、原 suffix 及 same-$\mu$ 路径保持。
每个外根 $x_{i,\alpha}^{\pm}$ 上，(16)—(17)使用同一共同外区 jets。
所有 ordered totals 现在对任意 outer u 和右三矩 n 都为零；
原有限 A 还使实际 self totals 为零。

记 R431 的参考 self cap 为 $s^\pm_{i,\alpha}$，
置 $\widehat s^-_{i,\alpha}=s^-_{i,\alpha}$、
$\widehat s^+_{i,\alpha}=-s^+_{i,\alpha}$。
负号使用的是实际 self total 零，不另重置积分常数。
则两真实通道统一写成
$$
\boxed{
\begin{aligned}
H_{d,i,\alpha}^{\pm}
&=a_i^3\left[
R_i\widehat s^\pm_{i,\alpha}
+\mathcal K_{V,n_{R,i}}(x_{i,\alpha}^{\pm};u_i)\right],\\
H_{e,i,\alpha}^{\pm}
&=-a_i^3\left[
T_i\widehat s^\pm_{i,\alpha}
+\mathcal K_{V,n_{T,i}}(x_{i,\alpha}^{\pm};u_i)\right].
\end{aligned}}
\tag{28}
$$
原完整 $s$ history 仍在(8)的确定系数内。
whole self 消的是平台二次项，不删仿射值；
参考 self cap 仍由 R407 的完整同矩路径给出，不说它仅由单点 jets 决定。

消 self 的真正组合因而是
$$
\boxed{
R_iH_{e,i,\alpha}^{\pm}+T_iH_{d,i,\alpha}^{\pm}
=a_i^3\mathcal K_{V,T_i n_{R,i}-R_i n_{T,i}}
(x_{i,\alpha}^{\pm};u_i).
}
\tag{29}
$$
真实 $a_i,R_i,T_i,n_{R/T,i},\xi_i,w_i$ 全部保留。
旧右侧 cap 的非 Euler 余积分已经由一个 actual 条件准确删除，
不是靠有限生成数或 q/D/E 的形式替换。

(29)对新 actual 成本与原响应列现在处于同一种明确局部表示；
这使 R432 的响应矩阵与目标可以直接比较。
但 actual 系数不必等于已列响应系数，其四个含 u 的项也不先置零。

## 8. 尚须求的精确像外商

为消歧，记
$$
\mathcal R_E=\mathcal R\cap\ker E,
$$
不是只取真权0的响应空间。
由(4)—(5)，$\mathcal R_E\subset\ker J^+$。
令 $\mathfrak P_C$ 表示(29)在全部真实根上的向量读出。
在同一个 fixed profile 库上，
$$
\boxed{
[\mathfrak P_C(V)]\in
\mathfrak P_C(\ker J^+)/
\mathfrak P_C(\mathcal R_E)
}
\tag{30}
$$
是响应不能改变的准确剩余类。
本稿没有宣称该商为零，也没有用 R432 的三十二条 $c_\tau=0$ 成本列代替整个 $\mathcal R_E$。
那些已知列在(17)上有严格来源；其外准确保留(18a)—(18b)的六个含 u 形式方向。若其它 $c_\tau\ne0$ 的 whole-E 相消响应覆盖它们，须按原式证明同一个成本的完整十八系数像，而非只为每个点分别配列。

即使(30)的实际目标为零，还需同时保持另一 self 通道(28)，
并将新的 partial 响应与完整 $J^+$ 在同一实际词中联调；
不能把两份各自满射的截面相加。
原全部内部 $A_f$ 通量、平台仿射连接、k 值闭合与十三行同规范仍欠，
任何允许的同一二阶 gauge 都不能改变已识别的内部通量不变量。

本次完成的是一个实际新增门与它的完整原式后果：
全 ordered 自然系数、whole E、原有限自然和原已付母库目标在同一点可成立；
一般 cap 的余项(9)因此字面归零；
全部跨包 partial 由(17)的七个实际低 jets 单项给出。
没有把完整第四 period 或固定度量嵌入族宣布完成。
