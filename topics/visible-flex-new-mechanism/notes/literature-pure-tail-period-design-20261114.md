# R56 真实 pure 第四的右尾系数 producer

日期：2026-11-14。独立新脚本：`scripts/literature_pure_tail_period.py`。原 `literature_range_profile_algebra.py` 及全部已有研究输出不改。研究编译只允许在 `Rogerhu12/math-research-public` 自己的 GitHub Actions 运行。

## 1. 科学目标与已证最低项

[R85](../results/R85-pure-fourth-leading-tail-is-an-exact-derivative.md) 从原始变系数 R56 证明：右端幂尾 $q=(c-\xi)^m$，$m\ge8$，其 pure 第四最低候选阶 $4m-9$ 是真实 histories 的准确总导数，零二阶矩阵与常值端芽已足使它的完整 period 为零。这不是第四成本正性或零成本解。

本 producer 直接保留 $4m-8$ 及以后系数，供寻找实际总导数、额外端项或真正对偶符号。它没有选择真实几何路径，也没有把一个非零 density 系数宣布为非零 period。

## 2. 数学与实现身份

物理定义为右端尾 $t=c-\xi$，$q=t^m$，$\xi\ge c$ 时为零；$c$ 是独立的 $s$ 常数。要求 $h>0$、$c+\omega$ 在真实路径上有正下界、$\omega_s=k_s/(2h)$。此前尚未选择某条满足这些条件的实际桥。

脚本没有重写 R56 forcing 公式：`TailCompiler.range_and_recover` 直接调用冻结模块的 `Compiler.forcing_range(..., recover=False)`。原 `Field` 的协变导数、全部 $T_s,T_{s\xi}$、$P,B,\eta_0,\mathcal R_H$ 以及 profile 齐次阶检查均实际执行。只把原来的自由 profile/Volterra 代数换成准确的有限 $t$ 多项式：

$$\partial_\xi=-\partial_t,\qquad I(t^p)=\int_r^\xi(c-\eta)^p\,d\eta=-\frac{t^{p+1}}{p+1}.$$

右端原函数没有任意常数。$\xi$ 的所有幂仍通过 $\xi=c-t$ 保留。每项同时记录 $t$ 幂和 profile 齐次阶；乘法、导数和原函数均不截断 $t$ 多项式。

恢复时，对每个完整 $t$ 系数引入一个真实 $s$ history，初值为零、导数为对应的原始 RHS。然后用原 R56 的分子式重建场。编译链为

$$Y=Y_q,\qquad Z_2=\mathcal I H(Y,Y),\qquad U_3=\mathcal I H(Y,Z_2),$$

$$H_4=-H(Z_2,Z_2)/16-H(Y,U_3)/4.$$

从不把 histories 逐点置零。$M=0$ 或 $\mathcal T=0$ 只作为将来真实路径的端点条件记录，未作为每个密度点的替代。

同时输出原始第四密度以及局部修正

$$\widetilde W=W+\lambda P,\qquad\lambda=(h_s z-h\omega_s)/h^2.$$

常值端芽上 $\lambda=0$，故修正不改变真实完整 period。脚本从原始 forcing 计算，再用准确 Laurent 展开核 R85 的两个 leading ODE、第四 leading 密度和总导数，共四个零恒等式。所有几何 derivatives 与历史 RHS 都保留；`tail_end` 仅在 $D_s$ 下取零。

## 3. 输出与证据范围

默认 $m=8$，最低阶为 $23$，准备读取 $23$ 到 $27$ 阶。输出三件：

- 主 JSON：实际完成/失败状态、R85 四条原式检查、DAG 与 history 规模、source SHA、预算及范围。
- `-expressions.json`：不超过 95 KB 的真实系数表达式。后阶项含实际 history 变量，明确只为 density/ODE。因大小省略的项有显式标记及准确表达式摘要。
- `-structure.json.gz`：全部未截断系数 DAG、每条真实 history RHS/初值、原始与修正第四密度、各检查 root。压缩文件小于 5 MB，同时绑定原始/压缩字节 SHA。

完整结构在可选 Laurent 展开前先写出。因此后续展开预算耗尽仍保存已经实际编成的原始系统；不会把未展开的系数当作零。没有执行路径求积、profile 数值积分、优化或嵌入诊断。

正检查为准确有理恒等式；非零余式只是保留 history 的原始 density 资料。尤其不能以 `state_...` 的形式独立性直接推断闭路径积分非零，也不能在端点需要 $M=\mathcal T=0$ 时继续把这些端点 state 当自由量。

## 4. 公开 Actions 命令

人工开发检查只涉及有限多项式和人为三角 ODE，不编真实 forcing：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_pure_tail_period.py \
  --check-only --out "$VISIBLE_OUT/pure-tail-development.json"
```

研究编译：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_pure_tail_period.py \
  --out "$VISIBLE_OUT/pure-tail-period.json" \
  --exponent 8 --next-orders 4 --max-seconds 240
```

默认保护为 600000 个 DAG nodes、每项 60000 个 Laurent terms、1500000 个 memoized terms、软 RSS 1800 MiB。预算停止返回 exit 2 和明确 partial；它不是数学条件失败。源码不导入数值优化器，不接受旧 private 输入。

## 5. 当前开发证据与后续

本地只运行了 [人工检查](literature-pure-tail-period-development-check-20261114.json)：右原函数符号、$\xi=c-t$、$c_s=0$、齐次阶、实际 $\omega_s$ 链式，以及人为 $b'=aC,u'=-a_1Cb$ 系统的 leading 总导数，共六项通过。没有在本地调用真实 `compile_tail`，也没有把人工通过写成研究结果。

实际输出后，优先分析 $4m-8$ 与 $4m-7$ 的完整系数是否仍可化为带正确端项的总导数；若有残留，再寻找对全部真实 $M=\mathcal T=0$ 环同号的真正评价泛函。任何符号结论还须区分 universal 算子与某个合法三矩 profile 圆，且不能从 R84 的倒行偶性或长度下界推出。
