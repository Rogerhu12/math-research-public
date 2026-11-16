# R840 联合交增补 — 全负水平的规范零 charge 标号

日期：2026-11-16。**状态：以下选择无关的全负水平映射和同一 $G_0$ 约束已证明。原高前缀与指定 forcing 仍开放。**

本注补
[完整联合交](2026-11-16-r840-full-primitive-and-ramification-ideal-intersection.md)，
不要求负水平点满足 $F_t\ne0$，不删双根、无穷远或固定角。

保该注的全部来源及记号：
$$
f_2K_a=F U_a+eV_a,\qquad
a\in\mathcal A_2=\operatorname{ann}_Z(f_2),
$$
$$
W=F(-V_a-\mathcal EK_a-2f_2B-e\mathcal EB+FC)
   +eK_a+e^2B.
\tag{1}
$$
这里 $e,f_2$ 的原零 charge 都为零，$F_0\ne0$。
对第一式取零 charge，得到
$$
F_0U_{a,0}=0,\qquad \boxed{U_{a,0}=0.}
\tag{2}
$$

## 1. 规范的全负水平标号

定义
$$
\boxed{
\beta_-(a)=[V_{a,0}]
\in\mathcal H_2^0/(F_0\mathcal H_1^0)
 \simeq H^0(Z_-,N^2|_{Z_-}),
\quad Z_-=C\cap H_-.
}
\tag{3}
$$
最后同构是 R833 的完整负水平限制序列，保全部概形长度。

此映射与 (1) 的所有提升选择无关。具体地：

- 同一个 $K_a$ 下，改变 syzygy 为
  $U'_a=U_a+eD_a,\ V'_a=V_a-FD_a$，
  仅将 $V_{a,0}$ 改成 $V_{a,0}-F_0D_{a,0}$。
- 改变 $K_a$ 为
  $K'_a=K_a+F A_a+eB_a$，
  可取 $V'_a=V_a+f_2B_a$，其零 charge 完全不变。
  再合第一种改变即涵盖任意选择。

所以 (3) 是原有限零化子的规范线性映射，不是按点任选的辅助数据。

## 2. 同一个原函数的 $G_0$

若 $(a,B,C)$ 通过完整联合算子 $\mathcal O=0$，
则 (1) 属于 $\mathcal I\cap\mathcal J$。
按原唯一分解
$$
W=\mathcal E_+^{-1}(F^2L)+G_0,
\qquad L\in\mathcal H_1^{>0},\quad G_0\in\mathcal H_3^0,
$$
$G_0$ 就是 $W$ 的零 charge。由 (1) 逐项读取，准确得到
$$
\boxed{G_0=F_0^2C_0-F_0V_{a,0}.}
\tag{4}
$$
因而 $G_0/F_0$ 是真正的 $\mathcal H_2^0$ 截面，并有
$$
\boxed{[G_0/F_0]=-\beta_-(a).}
\tag{5}
$$
式 (5) 在完整 $Z_-$ 上成立；这里的除法来自显示乘法恒等式 (4)，
没有在 $F_0$ 的零点另加极点。

特别 $a=0$ 时，取零提升，
$$
\boxed{G_0=F_0^2C_0.}
\tag{6}
$$
这比仅从 $W\in\mathcal I$ 得到的 $F_0\mid G_0$ 多一重真实限制。

对固定 $(a,B)\in\ker\mathcal O$，原 $C$ 仅差 $cF$，
所以同一个 $G_0$ 仅差 $cF_0^3$。它正是
$W\mapsto W+cF^3$ 的零 charge，必须与原第三长行
$6c e_P^3\eta$ 及第四短行使用同一个 $c$。
不能把 $C_0$、$G_0$ 或其各点导数独立选取。

在 $r=2$ 全 profile 中，
$$
\mathcal H_j^0=d^{j\mu_{d,1}}\,k[t]_{\le jz_-},
\qquad z_-\le2.
$$
(4)–(6) 都在这些真正空间内，
固定 $d$ 因子及无穷远零点没有改变。
它们也说明平滑负水平块中的 $G_0'(t_Q)$
是同一个全局 (4) 的导数，而非每个厚点的一份自由标号。

## 3. 联合算子的准确负水平冗余

完整算子的原代表为
$$
A_0=U_a-\mathcal EV_a-\mathcal E^2K_a
     -2f_3B-3f_2\mathcal EB-e\mathcal E^2B.
$$
由 (2) 及其余各项的正 charge，
$$
(A_0)_0=0,\qquad A_0\in\mathcal E\mathcal H_2 .
$$
R833 的实际全像定理因此给
$$
\boxed{
\mathcal O(\mathcal A_2\oplus\mathcal H_1)
 \subset
 \ker\!\left[
 H^0(Z,N^2|_Z)\to H^0(Z_-,N^2|_{Z_-})
 \right].
}
\tag{7}
$$
所以完整 $\mathcal O$ 可以准确使用 (7) 的目标；
其 $z_-$ 条负水平值行是恒零冗余。
这是来源算子的恒等式，不是原 $M$ 多出的左障碍，
也不取消其他负水平厚行或与 (5) 相连的全局条件。

(3)–(7) 不证明其余 $\mathcal O$ 行满射，
也不证明同 $K,H$ 的实际高前缀可解。
原完整十三行带、同一更高精度修正及所有 $\mathcal W_D$ 余列继续保留。
无新数学程序运行。
