# R239 附录：完整正 resolvent 对负源图缺陷的两费用校正

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文给出一个通用已证明的正算子引理，并用于原完整左/裸/右源度量。它以首头“裸向量加平坦向量”的实际缺陷支付进入负源图的校正，同时控制完整左费与两费用。它不控制普通完整右费，也不声称保留其他已经选定的源旗或两费用余图。普通 ISP 与 $N=M$ 仍为 OPEN。

## 1. 准确假设与裸/完整可行集的方向

设 $\mathscr R$ 为一个固定参数下的闭源 Hilbert 空间，$L,B,G$ 为其有界严格正算子。约定
$$
\mu(r)^2=\langle Lr,r\rangle,\qquad
\alpha(r)^2=\langle Br,r\rangle,
$$
$$
\lambda(r)^2=\langle G^{-1}r,r\rangle,
\qquad
\lambda_{\rm flat}(r)^2=\langle GLr,Lr\rangle,
\quad
\chi(r)^2=\alpha(r)^2+\lambda_{\rm flat}(r)^2.
\tag{1.1}
$$
假定
$$
\boxed{B\preceq G^{-1}.}
\tag{1.2}
$$
在本课题原完整右旗与低出生裸旗中，这是准确的实际方向：每条完整右可行链的低出生投影都是同源裸可行链，且投影不增范数，故 $\alpha(r)\le\lambda(r)$。平方并对所有源使用，即得 (1.2)。不把裸可行链自动当作完整可行链。

设 $P$ 为首源头的正交投影，$Q=I-P$，且已有共同首头分裂
$$
[P,B]=[P,G]=0,\qquad
B|_{P\mathscr R}=K,\qquad G|_{P\mathscr R}=K^{-1}.
\tag{1.3}
$$
完整左度量 $L$ 不被假定约化 $P$。负源图为
$$
\mathscr N=\ker[P(L+B)].
\tag{1.4}
$$
对原真实左源流，这是已经证明的准确像；下面的算子引理本身只用 (1.2)–(1.4)。

## 2. 裸度量归一与物理首头缺陷

定义
$$
u=B^{1/2}r,\qquad
H=B^{-1/2}LB^{-1/2}\succeq0,
\qquad C=B^{1/2}GB^{1/2}.
\tag{2.1}
$$
由 (1.2)，
$$
0\prec C\preceq I,
\qquad [P,C]=0,\qquad C|_{P\mathscr R}=I.
\tag{2.2}
$$
相应三个费用准确为
$$
\mu(r)^2=\langle Hu,u\rangle,
\alpha(r)^2=\|u\|^2,
\lambda_{\rm flat}(r)^2=\|C^{1/2}Hu\|^2.
\tag{2.3}
$$

定义首头缺陷的共同单位坐标
$$
\boxed{d(r)=P(I+H)u
=P B^{-1/2}(L+B)r.}
\tag{2.4}
$$
因为 $P$ 与 $B$ 交换，$d(r)=0$ 当且仅当 $r\in\mathscr N$。

在本课题的实际首头右链空间，$K=R_0^*R_0$，其中 $R_0f=e_0D^\dagger f$ 嵌入右首段。等距同构 $W_0=R_0K^{-1/2}$ 将 $Pu$ 变成首头裸最小链，将 $PHu$ 变成首头平坦链。因此
$$
\boxed{\|d(r)\|=\|a_0(r)+c_0^{\flat}(r)\|.}
\tag{2.5}
$$
这是两个向量在同一物理最小右空间内的和，而非两个范数的差。

仅由 (2.2)–(2.3) 也有
$$
\|d(r)\|\le\|Pu\|+\|PHu\|
\le\sqrt2\,\chi(r).
\tag{2.6}
$$

## 3. 完整正 resolvent 校正及两个准确界

给定任意 $d\in P\mathscr R$，定义
$$
u_t=(I+H)^{-1}d,\qquad t=B^{-1/2}u_t.
\tag{3.1}
$$
这使用整个正算子 $I+H$ 的逆，不是 $P$ 块的压缩逆。直接有
$$
d(t)=P(I+H)u_t=d.
\tag{3.2}
$$

由 $C\preceq I$ 和 $(I+H)u_t=d$，
$$
\begin{aligned}
\chi(t)^2
&=\|u_t\|^2+\|C^{1/2}Hu_t\|^2\\
&\le\|u_t\|^2+\|Hu_t\|^2\\
&=\|d\|^2-2\langle Hu_t,u_t\rangle.
\end{aligned}
$$
因此
$$
\boxed{\chi(t)^2+2\mu(t)^2\le\|d\|^2.}
\tag{3.3}
$$
另由正谱演算中的标量不等式 $x/(1+x)^2\le1/4$，
$$
\mu(t)^2
=\langle H(I+H)^{-2}d,d\rangle
\le\tfrac14\|d\|^2.
$$
合并得到
$$
\boxed{\chi(t)\le\|d\|,\qquad
\mu(t)\le\tfrac12\|d\|.}
\tag{3.4}
$$
常数不含 $\|L\|$、$\|B^{-1}\|$、任何有限头条件数或源旗夹角。

## 4. 把任意源送进准确负图

对原 $r$，在 (3.1) 中取 $d=d(r)$，并置
$$
r_-=r-t.
$$
则
$$
\boxed{r_-\in\mathscr N,\qquad
\chi(r_- )\le\chi(r)+\|d(r)\|,}
\tag{4.1}
$$
$$
\boxed{
|\mu(r_-)-\mu(r)|\le\mu(t)\le\tfrac12\|d(r)\|.
}
\tag{4.2}
$$
更精确的左向量比较为
$\|E^\dagger r_--E^\dagger r\|=\mu(t)$，其中 $E^\dagger$ 是该左最小原像映射。

在原源坐标中，这个校正具有简单的准确形式：令 $S=L+B$，则
$$
\boxed{t=S^{-1}PSr,\qquad r_-=S^{-1}QS r.}
\tag{4.3}
$$
两者都是互补的有界投影，但通常不是原物理内积或 $\mathfrak M=B+LGL$ 内积的正交投影。校正的像是 $S^{-1}(P\mathscr R)$，它可以包含非首头坐标。

尤其不能将 (4.3) 换成只加减首源头的
$\iota_0(K+L_{00})^{-1}\iota_0^*Sr$；后者虽然也消除负图缺陷，却没有本稿由完整正 resolvent 给出的两费用界。

无附加信息时，(2.6) 仍给通用范围
$$
\chi(r_- )\le(1+\sqrt2)\chi(r),\qquad
\mu(r_- )\ge\mu(r)-\chi(r)/\sqrt2.
\tag{4.4}
$$
若物理缺陷本来指数小，则 (4.1)–(4.2) 保留那个指数小量，不必使用 (4.4) 的粗界。

## 5. 精确适用边界

本稿同时支付完整左费、裸费和平坦费，因为 $\chi$ 已包含后两项。普通完整右费为
$$
\lambda(t)^2=\|C^{-1/2}u_t\|^2,
$$
而 $C\preceq I$ 没有提供对 $C^{-1}$ 的统一上界。因此未支付 $\lambda(t)$，也不能据此把这个校正无限向上延拓。

同样，(4.3) 没有自动保留任何另加的 $\mathfrak M$ 余图、模型支撑条件或既有 primitive 自由增量。若需要这些条件，须另行支付相应运输。

本文提供的是精确接口：一旦在同一物理首头右空间中证明向量缺陷 $a_0+c_0^{\flat}$ 很小，就能把该来源送入真正负图，同时只付该缺陷的左费和两费用。不能用单独的范数上界替代 (2.5) 所需的向量相消。
