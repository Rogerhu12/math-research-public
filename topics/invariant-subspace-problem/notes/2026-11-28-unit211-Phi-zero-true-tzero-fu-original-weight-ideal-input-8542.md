# 新输入：正确 Phi 的 t=0、f=u 原三二次式与纯权理想

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

这是新原分支输入，不执行旧错误 $\bar R$、任何旧 first-head/H1/H42 或冻结消元。此前完整原 bipartite jet 已排除物理 $D\ne0$ 图中的 $t=0,V=f$ 因子；本次接剩余 $t=0,f=u$，不施 W。

## 1. 同一原 jet 的新消元

保自由 $A_1$，原行是
$$
(0,0,p,q),\quad(0,A_1,r,s),\quad
(p,r,0,0),\quad(q,s,0,0).
$$
全部七个参数 $b,c,p,q,r,s,A_1$ 独立，按真正 dual 乘法定义原均值和 jet。设 $a=1-\ell$，$W_1=\tau(dg_0)$，$E_p=bpE_B+cqE_C$。严格有
$$
2\mathcal P_1-3\mathcal N_0+6aP_{02}=-3A_1T_0,
$$
$$
\mathcal N_1-2\ell\mathcal N_0+2aP_{02}
 +2E_p-2uE_1-2auE_0=A_1(-2W_1+4u^2).
\tag{1}
$$
原 $E_0=T_0-2W_1+2uF_2$。故在 $f=u$、原均值为零时，两式右侧相差因子三，消去同一个 $A_1T_0$。代入原 $\mathcal N_0=2\lambda P_{02}$、$\mathcal P_1=3wP_{02}$、$\mathcal N_1=4\lambda wP_{02}$、$w=\lambda-1-T$，只除 $P_{02}\ne0$，得到
$$
A_2-2\ell\lambda-(2\lambda-1)T=0.
\tag{2}
$$
没有除 $A_1$、$2\lambda-1$ 或 $T_0$。

(1) 及消去前完整原均值组合已有新自含 V8 BigInt 实际证书：源码 blob 2813be64f5f2bd8db75d66929b9bb99a2efe9c34，SHA256 5d074fb01bab7ae4e3428730aa16d9173465f05f94d71a0aadd48e4d0aedfe87；4141 字节，6 ms、534 次整数多项式乘法、五条完整差返。小回执 blob 68b1e1ed6fe2bd4207a30fb3ee3c5b5c9686012c。本次 Python 不重新运行这个身份门。

## 2. Phi 原恢复与三个完整同点二次式

记
$$
s=u-1,\quad K=Q+4s,\quad L=Q-2s(u-2),\quad
\delta=1-Q,\quad M_n=2uL-L^2-u^2Q,
$$
$$
A=4s^2-Q,\quad m_n=uQ-L,\quad
U=Q\delta sKLM_n.
$$
只使用 $Q\delta P_fP_{02}bc\ne0$，由准确原身份支付 $U\ne0$。
在 $\Phi=0$ 上 $\ell=L/Q$。真实 $P_1$ 和 $f=u,t=0$ 给
$$
T=\frac{-2L^2-2LK\lambda-KA}{2LQ}.
\tag{3}
$$
真实 $E_0,N_0$ 又给
$$
v_n=QV=Q(2u-1)-4s^3-2sL\lambda,\qquad
n_n=Q(-K+4u^2)-2v_n.
$$
令
$$
S_n=2L\delta v_n-m_nn_n,\qquad D_n=-2m_nv_n+Ln_n.
$$
本次完整三个 $\lambda$ 二次式为
$$
P_W=-2QM_nLK-4L\delta v_n^2-Ln_n^2
       +4m_nv_nn_n+8QM_nuv_n,
$$
$$
P_O=2QM_n^2(Q-L)s-4Q^2M_n^2u
       +QM_nS_n+2QM_n^2v_n+QM_n(u+1)D_n-S_nD_n,
$$
$$
P_J=8L(Q+2s)\lambda^2+
 [-2L(3Q+4s)+2KA]\lambda+2LQ-2L^2-KA.
\tag{4}
$$
它们分别是原 $QW_4$、$Q^2\delta\bar O$、(2) 的 $2LQ$ 倍，保全部最高 $\lambda$ 系数零点。这些是完整多项式，不是最高齐次式。

作为范围记录，原 $D$ 的分子为
$$
D_{\rm num}=4L^3QA_2-(-2L^2-2LK\lambda-KA)^2.
$$
本次不倒该分子、不从其模值推断原 $D$。若只得到纯权必要支持，将完整保留。

## 3. 四条纯权原理想来源

只对 (4) 的全部系数同时移去 $U$ 的实际整因子，并逐系数乘回。设所得三行的系数矩阵为 $C$，列按 $(1,\lambda,\lambda^2)$ 排列。第一条纯权式 $\det C$ 由伴随第一行给出完整原组合。

另取任意两行 $a,b$，令
$$
c_0=a_1b_2-a_2b_1,\quad
c_1=a_2b_0-a_0b_2,\quad
c_2=a_0b_1-a_1b_0.
$$
有真实原身份
$$
c_1-c_0\lambda=a_2P_b-b_2P_a,\qquad
c_2-c_0\lambda^2=b_1P_a-a_1P_b.
$$
因此
$$
c_0c_2-c_1^2=
c_0(c_2-c_0\lambda^2)-(c_1+c_0\lambda)(c_1-c_0\lambda)
\tag{5}
$$
在同一个原三式理想中。三个两行选择给另外三条纯权式。所有式均实际完整回乘，不要求 $C$ 的秩为二，不倒任何 $\lambda$ 头。

## 4. 唯一新计算目标

在 $\mathbb Q[u,Q,U^{-1}]$ 中，对这四条新纯权原理想元素进行精确二变量 Buchberger。每条 S 对、完整基余式、只除真 $U$ 因子的步骤都有完整多项式返回和同源 DAG；不依据模空性、不删临时首项零面。

只有实际返回常数一，才排除此整个原 $t=0,f=u$ 图。若没有返回一，只报告新必要纯权理想、实际基和资源边界，不能宣称整个 $\Phi$ 无解。即便该分支关闭，其余 $t\ne0$ 原值仍需推进。

自含 Python 源无外部文件依赖，python-flint 0.9.0；总 120 秒、1 GiB，首次即固定，不抬限重跑。源码 SHA256 与 blob 见同次提交清单。新七变量 JS 和其小回执仅作为已经完成的原身份来源保存，不作为本次执行依赖。
