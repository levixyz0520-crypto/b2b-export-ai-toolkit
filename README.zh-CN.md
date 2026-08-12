# B2B Export AI Toolkit（B2B 出口 AI 工具包）

[English](README.md)

B2B Export AI Toolkit 是一个开源、可接入 AI 的基础工具包，覆盖客户研究、买家资格评估、外联、报价分析、跟进与销售流程自动化。首批示例面向家具出口，但 Python 模块和结构化数据约定不绑定具体行业。

> **当前状态：** v0.1 仍处于早期阶段，仅提供确定性工具、示例和 Agent Skills；它不是自动销售系统、已验证的市场情报服务或生产级 CRM 集成。所有输出均需人工复核。

## 适用人群与项目动机

本项目面向出口销售与运营团队、开发者、研究人员和行业贡献者。出口工作常分散在表格、私人模板和不透明自动化中；本项目希望建立一个小型、可审计的公共基础层，未来可连接 AI 模型和业务系统，但不强制依赖任何服务。

## 安装

需要 Python 3.10 或更高版本。

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -e .
```

开发环境：

```bash
python -m pip install -e ".[dev]"
pytest
ruff check .
```

## 使用示例

命令接受 JSON 文件、内联 JSON 对象或纯文本，并输出稳定 JSON；无需 OpenAI API Key。

```bash
export-ai research examples/furniture-export/buyer-profile.json
export-ai qualify examples/furniture-export/buyer-profile.json
export-ai email examples/furniture-export/outreach-input.json
export-ai followup examples/furniture-export/followup-scenario.json
export-ai quote examples/furniture-export/quotation-input.json
export-ai sanitize '{"email":"fictional@example.invalid"}'
```

## 项目原则

1. 先确定性、后自主化：v0.1 行为应可复现、可复核。
2. 证据优先：区分来源明确的事实、假设与缺失信息。
3. 隐私设计：最小化输入，分享前脱敏，不提交私人销售数据。
4. 人工负责：外联、商业条款与重大判断必须由人审批。
5. 核心行业中立：家具只是示例，不是硬编码的数据模型。
6. 控制依赖：优先使用标准库和透明的数据约定。

## 项目结构

- `src/export_ai/`：确定性工作流模块与 CLI
- `examples/furniture-export/`：虚构且隐私安全的结构化示例
- `skills/`：带防护规则的 Codex/Agent 工作流
- `tests/`：核心逻辑与 CLI 测试

基础建设开始时，需求中提到的七个旧编号目录并不存在，因此没有删除或迁移已有知识。

## 路线图

- **v0.1：** 确定性核心、家具示例、Skills、测试和社区文件
- **v0.2：** 数据 Schema、可插拔数据源/模型适配器、更强校验、本地化和 CRM 安全接口
- **后续：** 可选集成、评估数据集、更多出口行业和工作流编排

路线图仅代表方向，不构成交付承诺。

## 参与贡献

请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [行为准则](CODE_OF_CONDUCT.md)，大型改动前先提交 Issue。欢迎贡献缺陷修复、测试、翻译、合规行业示例和文档改进。

## 隐私与安全

只能使用虚构数据或已获适当授权的数据。严禁提交客户记录、私人联系人列表、凭据、API Key、专有报价、私人通信或公司机密。分享前请脱敏，并核验所有生成的声明。安全漏洞请按 [SECURITY.md](SECURITY.md) 私下报告，不要创建公开 Issue。

## 许可证

本项目采用 [MIT License](LICENSE)。
