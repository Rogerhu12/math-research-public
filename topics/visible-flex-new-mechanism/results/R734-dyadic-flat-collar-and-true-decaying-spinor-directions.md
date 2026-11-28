# R734　平帽上允许非轴等距方向的真实二进径尾

固定外半径 $b=11/50$，外领宽 $L_0=1/512$，$L_n=L_0\,2^{-n}$，$x=b-r=L_n t$，$1/2\le t\le1$。令 $W>0$。本节提供一条确切的非解析母线和每个固定 $j\ge2$ 的一维真线性边界数据，可送入内侧求解器；未给出全频一致逆或非线性等距闭壳。

## 可拼到平帽的母线

取 $D=256,\ \delta_n=L_n/b<1/32$，$c=3/4$，$S(y)=0$ ($y\le0$)、$S(y)=6y^5-15y^4+10y^3$ ($0<y<1$)、$S(y)=1$ ($y\ge1$)。在本胞内置
$$
 H_n(t)=\tfrac12[1-S((t-1/2-\delta_n/2)/(\delta_n/2))]
        +S((t-c+\delta_n)/(2\delta_n))
        -\tfrac12 S((t-1+\delta_n)/(\delta_n/2)).
$$
三个过渡层不交。$0\le H\le1$，两个胞端各有真邻域为 $1/2$。向外走时先经过 $H=1$ 高台，再经过 $H=0$ 低台。定义
$$
 w(r)=W x^5(D/x^2)^{H_n(t)},\qquad h(r)=-\int_r^b w(s)\,ds .
$$
两个胞给接点两侧同一函数 $W\sqrt D\,x^4$。全胞 $0<w\le WD x^3$。因 $|S'|\le15/8$，有 $|H_r|\le (15/4)b/L_n^2$，微分 $\log w$ 得
$$
 |w'|\le WD x^3\bigl(5/x+(15/4)bL_n^{-2}\log(D/x^2)\bigr)
       \le C W x(1+|\log x|).
$$
故 $h,h',h''$ 在 $b$ 全为零，$F_0=r e_r+h e_z$ 真正 $C^2$ 拼平帽。两主曲率的绝对值由 $|w'|,\ |w|/r$ 分别控制。改变 $W$ 可在这条真实尾上统一调小二者。这里用有限阶控制；$w$ 在越端无限多个高/低台之间转换，并非有限段径向实解析延拓至帽圈。

## 确切传递与可计算的误差

对固定整数 $j\ge2$，记 $k=j^2,\ C_j=k(k-1)$。真实径方程为
$$
 (w f')'-k(w'/r)f=0.
$$
置 $F=(b/r)^k f$，$Y=(r/b)^k w(f'-kf/r)$。直接微分得 $F'=(b/r)^{2k}Y/w,\ Y'=-C_j(r/b)^{2k}wF/r^2$。在第 $n$ 胞用 $Z=Y/(W L_n^4)$、外行时间 $\tau=1-t$。无损系统为
$$
 (F,Z)_\tau=\begin{pmatrix}0&A_n\\-B_n&0\end{pmatrix}(F,Z),\quad
 A_n=(b/r)^{2k}t^{-5}e_n^{H},\quad
 B_n=B_0(1-L_nt/b)^{2k-2}t^3e_n^{1-H},
 \quad e_n=L_n^2 t^2/D,\quad B_0=C_jD/b^2.
$$
不出现对 $H$ 的导数。胞末 $Z$ 改用下一胞尺度，正好乘16。设
$$
 A=\int_{1/2}^{3/4}t^{-5}\,dt,\quad B=B_0\int_{3/4}^1t^3\,dt,\quad
 M_\infty=\operatorname{diag}(1,16)
 \begin{pmatrix}1-AB&A\\-B&1\end{pmatrix}.
$$
高台的下剪切先作用，低台的上剪切后作用。所有实际 $M_n$ 及极限行列式均为16。

以下给不用未知渐近常数的保守界。若 $\delta=L_n/b\le1/(8k)$，则 $1\le (1-L_nt/b)^{-2k}\le2$，其偏离1至多 $8k\delta$；$0\le1-(1-L_nt/b)^{2k-2}\le2k\delta$。非纯台和极限跳跃的差只发生在总长度至多 $4\delta$ 的三层。所有 $A_n\le64,\ B_n\le B_0$，在纯台上错误的剪切系数多得因子 $e_n\le L_n^2/D\le\delta$。故对诱导无穷矩阵范数，
$$
 \int_0^{1/2}\|G_n-G_\infty\|_\infty\,d\tau
 \le C\delta,\quad C=8(64+B_0)+256k+2kB_0+64+B_0 .
$$
$G_\infty$ 为上述两种纯剪切生成元。它的基本矩阵及逆每一点的范数都至多 $K=(1+A)(1+B)$。写 $U_n=U_\infty V$，对 $V'=U_\infty^{-1}(G_n-G_\infty)U_\infty V$ 用积分形式，即得
$$
 \|M_n-M_\infty\|_\infty\le16K[\exp(K^2 C\delta_n)-1]=:\epsilon_n .
$$
右式对每一固定 $j$ 是有效的 $O_j(L_n)$。坡的导数观察含 $1+n$，这里没有这一因子，因为传递只读 $H$ 的值和三层的真实长度。

## 真吸引线、方向包围和端正则性

$AB\ge256\cdot12 b^{-2}(1/4)(1/4)(3/4)^3>1600$。令 $T=17-AB$，稳定负根取无消去式 $\lambda_s=32/(T-\sqrt{T^2-64})$、$\lambda_u=T-\lambda_s$。二者相异，$|\lambda_s|<1/32,\ |\lambda_u|>512$。对每个根可取向量 $(A,\lambda-1+AB)$；矩阵 $P$ 以稳定、不稳定向量为两列，可分别缩放但须保持次序。选 $n_*$ 使 $\delta_{n_*}\le1/(8k)$ 且 $\|P^{-1}\|_\infty\|P\|_\infty\epsilon_{n_*}\le1/128$。此为有限可计算门。此后在 $P$ 坐标
$$
 P^{-1}M_nP=\begin{pmatrix}\lambda_s+e_{11}&e_{12}\\e_{21}&\lambda_u+e_{22}\end{pmatrix},
 \quad |e_{ij}|\le1/128.
$$
末方向的斜率 $H^+=z_u^+/z_s^+$ 取 $[-1,1]$，前一斜率准确为
$$
 H=\frac{H^+(\lambda_s+e_{11})-e_{21}}
         {\lambda_u+e_{22}-H^+ e_{12}} .
$$
分母绝对值至少 $|\lambda_u|-2/128$。所得 $|H|<1$，其对 $H^+$ 的 Lipschitz 常数至多 $16/(|\lambda_u|-2/128)^2<1$（实际行列式）。逐胞反传闭区间形成嵌套区间，直径几何趋零，故给唯一真实稳定射线。沿这条线外行，稳定坐标每步至多乘 $|\lambda_s|+2/128<1/16=:\gamma$。另一独立方向不能同样衰减，因为两解行列式每胞放大16。有限较内侧的 DtN 以整条齐次线反传；只有分母的确离零时才使用 $f'/f$，遇零用齐次坐标。

胞内真实传播有与 $n$ 无关的界（固定 $j$），因 $A_n,B_n$ 积分有界。故 $F,Z=O_j(\gamma^n)$，且 $|Y|\le C W L_n^4\gamma^n$。$w\ge W x^5$ 给 $|f'|=O_j(\gamma^n/L_n)$。由 $f''=-(w'/w)(f'-kf/r)$ 和上述 $\log w$ 的导数界，
$$
 |f''|\le C_j(1+n)\gamma^n/L_n^3\ \longrightarrow 0,
$$
因为 $\gamma\,2^3=1/2$。$f,f',f''$ 全圈拼零，且在任何有限处该解不恒零。这是 $C^2$ 真非轴尾解，未给 $j\to\infty$ 一致门或任意高径阶全平性。

## 实际 Cartesian 应变与闭纬圈参数

取 $U=(r w f'-k w f)/(k-1)$，$V=-U/j$，置
$$
 D_j=U\cos(j\varphi)e_r+V\sin(j\varphi)e_\varphi+f\cos(j\varphi)e_z.
$$
上述真 ODE 给 $U'=-w f'$、$U+jV=0$、$rV'-jU-V-jwf=0$。这正是 $F_0$ 的三条完整线性化 Gram 方程。$U=r(b/r)^kY/(k-1)$、$U''=-w'f'-wf''$ 及前节界给 $U,U',U''\to0$，所以整个向量场是 $C^2$ 帽接。$r^{-1}\partial_\varphi D_j=-d\sin(j\varphi)e_r+e\sin(j\varphi)e_z$，其中 $d=(k-1)U/(jr),\ e=-jf/r$。

[R726](R726-closed-spinor-fourier-and-complete-common-metric-residuals.md) 的圆基 $a=\cos(\psi/2), b_s=-\sin(\psi/2)$ 有 $J=1$。令 $u=d\sin(j\psi),v=e\sin(j\psi)$，取
$$
 \dot a_R=b_su/2,\quad \dot b_R=-au/2,\qquad
 \dot a_I=b_s v/2,\quad\dot b_I=-av/2 .
$$
这只用 $j\pm1/2$ 的全部半频，无 $1/2$ 基系数；各自与规范化圆基正交。直接代 Hopf 公式给 $\dot J=\dot\Phi=0$ 和 $\dot V_{\rm Hopf}=r^{-1}\partial_\varphi D_j$。源位移的角均值为零（$j\ge2$），重心的一阶变化亦为零。把四组非基系数的半数作为 R726 真立体坐标的切向量，令参数沿 $q$ 的直线变化，真实 $C=h e_z$ 固定。每个小 $q$ 均有精确闭纬圈、真平帽两阶接和材料反射；其在原固定 $g=(1+w^2)dr^2+r^2d\varphi^2$ 上三条实际 Gram 残差一致为 $O(q^2)$，因线性项确切消失且 $r$ 有正下界、所有径向二阶有界。多个有限 $j$ 可以在同一切向量中叠加。这里得到一个已知真实固定度量的非线性修正输入，不把二阶缺陷当作准确等距、全时间几何或整壳宏观运动。

连续尾线夹逼、向内的有限胞原算子、同一材料点的实际曲率及闭圈系数属于不同的费用。任何有限浮点 ODE 的中心读数必须单列；只有真正有向包围传递才可给相应的严格有限边界区间。此构造的非线性补偿、中央双核、全频逆、宏观位姿与 reach 仍待完成。
