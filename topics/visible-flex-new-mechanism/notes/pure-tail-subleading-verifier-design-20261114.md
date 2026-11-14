# R88 下一幂尾：消费公开 DAG 的准确核验入口

日期：2026-11-14。新增独立程序 `scripts/literature_pure_tail_subleading_verify.py`。旧 R56 编译器、首轮 tail producer 和其所有实际输出保持原样。研究模式只在本公开仓库 GitHub Actions 中运行；本地只执行了小型人工三角 ODE 检查。

## 1. 核验对象与真实第一积分

[R88](../results/R88-pure-fourth-subleading-tail-is-an-endpoint-potential.md) 给出一般 $m\ge8$ 的纸面公式。令 $p=2m-3$，从原 `completed` 系数取

$$b_0=[t^p]\widetilde W_2,\quad b_1=[t^{p+1}]\widetilde W_2,
\quad u_0=[t^{3m-6}]\widetilde W_3,\quad u_1=[t^{3m-5}]\widetilde W_3.$$

指定端点势为

$$F=\frac{p^3}{8m^2(m-1)}b_0^2b_1
+\frac{3p(3m-5)}{16m(m-1)}b_0u_1.$$

程序核验第 $4m-8$ 原始 completed density $D$ 是否满足

$$D-D_sF=Q_{\rm cert}\,I_0,\qquad
I_0=u_0+\frac{a_{mp}}{2a_{mm}}b_0^2.$$

这里先独立重新验证 $D_s I_0=0$，并验证零初始 histories 与常值 scalar 初始 germ 给 $I_0(0)=0$。只有这两项都通过，才允许使用 $I_0=0$。消元是对原始 leading third history 的**首一线性多项式除法**，不除以任何可能为零的函数、不改变其他 histories，也不把所有内部状态设为端值。

除法后从原 DAG 两边重新展开一次，必须得到同一个余式。若余式为零，压缩证书同时保存原始扩展 DAG、真实 state RHS、指定根、准确有理商与空余式。若余式非零，报告准确保留它，只能否决这条指定身份，不能排除别的端点势。

## 2. 实际输入与身份

首轮公开输入是 run `43635287277`、source `f3102464c049e13cbf306b29cb31cd3d38eb5607` 的

- `notes/actions-43635287277-1-pure_tail_period/pure-tail-period.json`；
- 同目录 `pure-tail-period-structure.json.gz`。

原报告已完成，保留 4681 个 coefficient DAG 节点和 14 个 genuine histories；其 R85 四条检查均为准确零。本程序不把这些信息当作新的第 24 阶结果。

它验证输入报告里的 packed/raw 长度与 SHA256，重建原 DAG 的节点编号与全部 state RHS，并要求实际导入的原 tail/R56 源码字节 SHA 与输入绑定一致。输入仅允许在本题已发布 `notes/` 路径下。没有研究 forcing 编译、几何路径选择、profile 重拟合或数值积分。

## 3. 可直接使用的公开命令

人工开发检查：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_pure_tail_subleading_verify.py \
  --check-only --out "$VISIBLE_OUT/pure-tail-subleading-development.json"
```

实际消费：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_pure_tail_subleading_verify.py \
  --report topics/visible-flex-new-mechanism/notes/actions-43635287277-1-pure_tail_period/pure-tail-period.json \
  --structure topics/visible-flex-new-mechanism/notes/actions-43635287277-1-pure_tail_period/pure-tail-period-structure.json.gz \
  --out "$VISIBLE_OUT/pure-tail-subleading.json" \
  --max-seconds 240
```

需 sparse-checkout 的新输入只有上述实际目录；导入源是本题 `scripts/`。研究命令同时核 `GITHUB_ACTIONS=true` 与精确公开仓库名。

输出为小主报告、低于 95KB 的可读表达式与低于 5MB 的完整 `.json.gz` 证书。可读项若因大小省略会显式标记，完整证书仍保留。资源预算只限制展开，不把未完成或省略项称为零。

## 4. 已执行的人工检查与严格范围

本地检查使用四个任意人工 histories，选择 $b'=G,u'=-2bG$，并构造一个故意含非零 $I_0H$ 的 density。它验证：原节点/RHS 重建、真实第一积分导数与初值、首一消元、错误 density 保留余式、非零初值拒绝，以及 $c$ 的 $s$ 常量身份。没有读取实际结构或编译 R56 研究目标。完整开发 JSON 已记录源码 SHA。

若实际第 24 阶通过，只支付 R88 的这一准确端点系数。结合常值端芽与总 $M=0$，端点势因 $b_0=0$ 消失；更高阶、完整 $V_4/P_0$ 的零性或符号以及正长度零成本环仍未支付。单个 $m=8$ 的计算也不替代 R88 对一般 $m$ 的纸面证明。
