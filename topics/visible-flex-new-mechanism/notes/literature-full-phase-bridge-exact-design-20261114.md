# 完整外槽第三桥与两谐波 P1：准确编译设计

日期：2026-11-14。接口与准确代数设计；真实目标尚未在本机编译。人工 toy 不生成研究算子、profile 值、几何或 ODE。实际运行只允许本公开仓库的 GitHub Actions。

主入口：`scripts/literature_full_phase_bridge_exact.py`。独占辅助层：`scripts/literature_colored_profile_algebra.py`。复用已经发表的 R56 完整恢复、R73 局部第三密度、R71 交换子、R77 三次速度可达、R78 全相位条件及 R79 闭水平 C1 可达；不更改已有 pure、local 或 word 程序。

## 1. 此次实际计算回答什么

原 pure 研究只处理 $-4$ 模式；R78 已证明还必须处理独立的 $-2$ 模式。本入口在**同一个参数向量**下联合匹配二者，并显式编译

$$\mathcal T(a;b,c),$$

外槽 $a$ 与两个对称内槽 $b,c$ 独立。只把 $\mathcal T(q;q,q)$ 当输入会丢失本次需要的资料；程序没有用对角三次极化冒充全算子。

目标是标准 $h=1,d=0,k=\pm1$ 常态的完整 $P_1$，已除去公共正 bulk 时间 $\ell$。正段 second 算子因此用 $r_+$，负段用 $-r_+$；这一公共缩放不改变零条件。全部 profile 同在共同右 collar 为零，$I$ 为物理半线内的共同紧区间。实际有限控制词选定后还须让同一 $I$ 覆盖其全部 $\xi+\omega>0$ 范围。

计算不是把 pure positive 关系复制到其他模式。两个模式的局部目标都由原始完整恢复生成；对每个控制算子使用 R78 的同一组 $\Delta\mathcal K,\Delta\mathcal L$，再取两个准确 Laurent 系数。

若输出准确正关系，它支付的是全函数 $P_1$ 的两个复模式及由准确种子决定的常数模式。它不支付 $P_0$、第四 ruling、低阶双 collar、无限阶或收敛，也不生成可打印的闭嵌入曲面。

## 2. 两个真实局部目标

对两个常态分别调用原 R56 的六张量、五谐波编译。所有 $s$ 微分先使用真实 second/third history RHS，然后才把**传入的历史值**置零。这与 R62 的完整本地漂移相符；没有把 $W_s$ 或 $U_s$ 置零。

把两态相加，保留 $-4,-2$ 两个目标。其余三个模式用于准确检查 $\theta=0$ 种子的总和恒零。这里没有有限网格、profile 积分或数值 seed cancellation。

在一般真实 geometry 上，另外生成

$$B_{bc}=\mathcal I H(Y_b,Y_c),\qquad R\{H(Y_a,B_{bc})\}.$$

同样先微分全部历史 RHS、后置历史值零，得到 R73 的完整局部 $\mathcal C_s(a;b,c)$，其中变 profile 所需的 $\Psi_s(a,r_s(b,c))$ 已由真实链式微分保留。程序按每个 profile monomial 检查多次数恰为 $(1,1,1)$，并核对内槽交换身份。

真实 geometry 关系始终是

$$\omega_s=k_s/(2h).$$

随后只在 geometry Laurent/log 多项式上做准确分解

$$\mathcal C_s=D_s(P_{\rm acc}+P_h)
+A(S)(k_sh_{ss}-h_sk_{ss})
+\sum_{j=0}^3B_j(S)h_s^{3-j}k_s^j
+R(S)k_s. \tag{1}$$

原始 profile 表达式保留，不用其约简代表替换它们。整个重构再次检查；这使正关系可以回到原始编译根验证。

## 3. 实际可达控制列

列分三组，全部为完整三线性算子。

1. R71 的至多 28 个 $\Phi_i(a,\Phi_j(b,c))-\Phi_j(a,\Phi_i(b,c))$。任意有限幅值用有限个局部小参数真环复制，不把超出局部 IFT 范围的参数塞进单个小环。
2. R77 证明可达的 $A(S)$ 和四个 $B_j(S)$ 的完整 geometry 系数。每个系数是一个实际有限控制方向；不只是把它们当任意形式矩。
3. R79 证明可达的闭水平 C1 空间。若 $R$ 是 (1) 的线性残项，使用

$$\partial_h(h^2R_h),\qquad
(R+hR_h)_\omega+2(h^2R_h)_k \tag{2}$$

的全部 geometry 系数。

式 (2) 是有实际控制证明的整个函数空间；不是把所有 $h^a k^b\omega^c k_s$ 矩独立开放。程序特别不重用已失败的“三个线性参考列已经足够”假设。

零列和相同准确 word 代表的重复列可删除。未声明剩余列在实际函数空间独立。联合消元的 rank 也只是准确代表矩阵的 rank；未产出正关系不是实际函数非成员定理。

## 4. 完整 C1 基准，而非三个自由矩

取 $a=2+\sqrt3$，所以 $a^{-1}=4-a$，$a+a^{-1}=4$。使用五段真实 scalar 路径

$$\begin{array}{c|c|c}
\text{段}&h&k\\\hline
1&1\to a&1\\
2&a&1\to0\\
3&a\to a^{-1}&0\\
4&a^{-1}&0\to-1\\
5&a^{-1}\to1&-1.
\end{array}$$

每段可用同端 flat step，端芽平滑拼接。$\omega$ 从 1 开始真正积分 $dk/(2h)$。在两个 $k$ 段上分别为

$$\omega=1-\frac1{2a}+\frac{k}{2a},\qquad
\omega=1-\frac1{2a}+\frac{ak}{2}.$$

所以末值准确为 $-1$；没有清零或补写末值。$P_h$ 以 $h=1$ 归一，首末都为零；$P_{\rm acc}$ 因端速度平坦也为零。线性签名因此是**全部** $R(h,k,\omega)dk$ 的两段准确积分，而不是只取 $\int dk,\int h^{\pm1}dk$。

每个系数的积分在

$$\mathbb Q(a)[\log a],\qquad a^2-4a+1=0$$

中准确进行。$\log(a^{-1})=-\log a$。输出按 $a^j(\log a)^m$、$j=0,1$ 分量列出联合函数目标。逐分量恒零是充分条件；程序不使用关于这些实常数的额外代数独立性主张。

### 为什么这个 scalar 原料确能代表实际零矩桥的第三端点类

五段 scalar 路径本身没有被宣称为 frame 闭合或 $M=0$。选一座 R70 已保证存在的真实同端口零矩桥。它和这五段 scalar 路径的 C1 积分差，是闭水平 scalar 环的积分，故属于 R79 空间。两者的 C3 积分均属于 R77 空间。真实零矩桥在 R73 中保留的反对称矩阵历史属于 R71 交换子空间。故该桥的完整第三算子与本节完整 C1 签名之差，属于第 3 节的**实际可达**空间。

R72 同 scalar 的 frame 修正可安排 $M=\mathcal T=0$，但不因此宣称其局部 $\int\mathcal C$ 为零；相应局部与历史之差仍已包含在上述论证中。位置端点自由，由同一修改后单 P 的 R45 四块结构处理。

因此，若本次原式验证给出“C1 基准 + 可达列”恰好抵消完整局部目标，就存在同端口的有限真实桥实现该第三算子。辅助大圈数和不同控制词的成本仍保留；没有由此产生厚度或嵌入保证。

## 5. 联合两模式消元及正关系验证

第三算子 $T$ 的响应使用 R78：

$$\Delta\mathcal K(D_1,D_2)=T(\mathcal A D_1;D_2)+T(\mathcal A D_2;D_1),$$

$$\begin{aligned}
\Delta\mathcal L(x\odot y,D)={}&-2T(x;y\odot\mathcal A D)-2T(y;x\odot\mathcal A D)\\
&+2\mathcal A(x,T(y;D))+2\mathcal A(y,T(x;D)).
\end{aligned}$$

令 $q=f+ig$，$F=f^2$，$d=(q^2+\bar q^2)/2$。每个控制列同时输出

$$\Delta P_{1,-4}=\Delta\mathcal Q(q^2,q^2)/16,$$

$$\Delta P_{1,-2}=-\{\Delta\mathcal L(F,q^2)+\Delta\mathcal Q(d,q^2)\}/4,$$

其中 $\Delta\mathcal Q=\Delta\mathcal K-\operatorname{Sym}\Delta\mathcal L$。联合向量的行键含模式号，所以消元不可能为两个模式偷偷选择不同参数。

若某个场扩张分量得到正关系，程序重新合成**原始第三模板**：完整基准减去原始控制列的线性组合，再重新计算两模式响应、加上原始局部目标，并用新的有锚 word 实例核两个残差严格零。不能仅以已有代表矩阵的余项零为最终证据。

输出包括全部控制列标签、源模板哈希、联合响应哈希、共同参数、每个场分量的未约简余项预览或 fresh 原式零证据。只保有限预览；大中间 DAG 不进入仓库。

## 6. 带颜色的准确原函数层

辅助层的 jets 带颜色，$a,b,c,q,\bar q$ 不混同。替换是同时进行的，且把任意内层右原函数一起替换；与真实 $\xi$ 微分交换。

word 使用有符号原函数 $I(F)=\int_r^\xi F$。全深度 shuffle 保持真实公共右锚。分部规则

$$I(D F\,I_w)=F I_w-I(FD I_w)$$

在 $w$ 非空时右边界因 $I_w(r)=0$ 消失；$w$ 空时只在 $F$ 有正 profile 次数、故在右 collar 为零时使用。纯 $\xi$ 多项式的无词原函数需要显式端点常数，程序拒绝无条件丢掉它。所有左尾保持。

最高 jet 分部只有在该导数阶数在**所有颜色中恰好出现一次**时启用。遇环保留原始 word，不宣布零；层仍故意不完备。负结果仅为未产出准确身份。

## 7. 开发、资源与实际命令

人工 toy 已仅检查：颜色乘法分部、三层 shuffle、替换与导数/原函数交换、相同对角但不同外槽的反例、两模式共用一个参数、二次实数域的准确算术，以及 R78 在完整 15 维人工 $\mathcal K/\mathcal L$ 基上的模式公式。没有实际编译研究目标。

公开开发入口：

```sh
python topics/visible-flex-new-mechanism/scripts/literature_full_phase_bridge_exact.py \
  --toy-only --output /tmp/full-phase-bridge-development.json
```

实际公开 Actions 命令：

```sh
python topics/visible-flex-new-mechanism/scripts/literature_full_phase_bridge_exact.py \
  --max-seconds 300 --max-coefficient-nodes 600000 \
  --max-profile-atoms 160000 --max-terms 120000 --max-rewrites 750000 \
  --memory-mib 2048 --rational-bits 8192 --max-output-bytes 700000 \
  --output /tmp/full-phase-bridge-exact.json
```

研究入口同时核 $GITHUB\_ACTIONS=true$ 和准确公开仓库名。RSS 是代码检查点的软轮询阈值；有理位长界用于消元；不把它们描述为操作系统硬上限。超时、规模或实现门失败均写带阶段的 partial 回执并退出 2，不冒充数学否定。输出过大先移除人读预览，仍过大则只写长度、哈希、身份及明确失败回执。

期望单个 JSON 小于 700 KB，不保存大数组或控制网格。全部依赖与主入口 SHA256、GitHub source/run 身份进入报告。真实编译完成后依据具体余项决定下一步，不自动加预算或重复同一目标。
